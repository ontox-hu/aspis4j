from unicodedata import name
from doctest import DocFileCase
import requests
import pandas as pd
import numpy as np
import json
import time
from py2neo.ogm import Graph, Node, GraphObject, Property, RelatedTo


NEO4J_HOST     = "c61a7d98.databases.neo4j.io"
NEO4J_PORT     = "7687"
NEO4J_USER     = "neo4j"
NEO4J_PASSWORD = "yY6Zqq_j2Y_6UjtGXidKjD_DjQUP1FQ04DEfWabB3j4"

graph = Graph( 
    host     = NEO4J_HOST,
    port     = NEO4J_PORT,
    user     = NEO4J_USER,
    password = NEO4J_PASSWORD,
    scheme   = "neo4j+s"
)

df = pd.read_csv('./CTDChemicals003.csv', skiprows=27)
df.rename(columns = {'# ChemicalName':'ChemicalName'}, inplace = True)
df.drop([0], inplace = True)
NumItems = len(df.index)

tx = graph.begin()

tic = time.perf_counter()
for i in range(NumItems):
    ChemicalID = df.iloc[i, 1].split(":")
    ChemicalID = ChemicalID[1]
    ChemicalName = df.iloc[i, 0]
    if type(df.iloc[i, 2]) == np.float64 or type(df.iloc[i, 2]) == float:
        if np.isnan(df.iloc[i, 2]):
            CasRN = ""
        else:
            CasRN = str(df.iloc[i, 2])
    else:
        CasRN = df.iloc[i, 2]
    tx.create(Node("Chemical", ChemicalName=ChemicalName, ChemicalID=ChemicalID, CasRN=CasRN))
    if i%100==0:
        graph.commit(tx)
        tx = graph.begin()
        toc = time.perf_counter()
        print(f"Executed {i:d} queries in {toc - tic:0.4f} seconds")

graph.commit(tx)
toc = time.perf_counter()
print(f"Executed {NumItems:d} queries in {toc - tic:0.4f} seconds")

Result = graph.run("MATCH (n) RETURN count(n)").data()
print(Result)