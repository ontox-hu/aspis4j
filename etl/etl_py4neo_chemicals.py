from unicodedata import name
from doctest import DocFileCase
import requests
import pandas as pd
import numpy as np
import json
import time
from py2neo.ogm import Graph, Node, GraphObject, Property, RelatedTo
from settings import NEO4J_HOST,NEO4J_PASSWORD,NEO4J_PORT,NEO4J_USER

print(NEO4J_HOST)
print(NEO4J_USER)
print(NEO4J_PASSWORD)


graph = Graph( 
    host     = NEO4J_HOST,
    port     = NEO4J_PORT,
    user     = NEO4J_USER,
    password = NEO4J_PASSWORD,
    scheme   = "neo4j"
)

try:
    graph.run("MATCH () RETURN 1 LIMIT 1")
    print('Connection to Neo4j DB succesfull')
except Exception:
    print('No connection to Neo4j DB')
    quit()

df = pd.read_csv('./etl/CTDChemicalsAll.csv', skiprows=27)
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