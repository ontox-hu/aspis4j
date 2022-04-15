from unicodedata import name
from doctest import DocFileCase
import json
import requests
import pandas as pd
import numpy as np
import time
from py2neo.ogm import Graph, Node, GraphObject, Property, RelatedTo, NodeMatcher
from py2neo.data import Relationship
from settings import NEO4J_HOST,NEO4J_PASSWORD,NEO4J_PORT,NEO4J_USER

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

matcher = NodeMatcher(graph)

df = pd.read_csv('./etl/CTDChemicalsDiseases.csv', skiprows=27)
df.rename(columns = {'# ChemicalName':'ChemicalName'}, inplace = True)
df.drop([0], inplace = True)
NumItems = len(df.index)
LowIndex = 10000
HighIndex = NumItems
CommitQueries = 300

# tx = graph.begin()

tic = time.perf_counter()
# for i in range(LowIndex, HighIndex):

#     ChemicalID = df.iloc[i, 1]
#     chemical = matcher.match("Chemical", ChemicalID=ChemicalID).first()
#     if chemical==None:
#         ChemicalName = df.iloc[i, 0]
#         if type(df.iloc[i, 2]) == np.float64 or type(df.iloc[i, 2]) == float:
#             if np.isnan(df.iloc[i, 2]):
#                 CasRN = ""
#             else:
#                 CasRN = str(df.iloc[i, 2])
#         else:
#             CasRN = df.iloc[i, 2]
#         chemical = Node("Chemical", ChemicalName=ChemicalName, ChemicalID=ChemicalID, CasRN=CasRN)
#         tx.create(chemical)

#     GeneID = str(int(df.iloc[i, 4]))
#     gene = matcher.match("Gene", GeneID=GeneID).first()
#     if gene==None:
#         GeneSymbol = df.iloc[i, 3]
#         gene = Node("Gene", GeneID=GeneID, GeneSymbol=GeneSymbol)
#         tx.create(gene)

#     GeneForms = df.iloc[i, 5]
#     Organism = df.iloc[i, 6]
#     if type(df.iloc[i, 7]) == np.float64 or type(df.iloc[i, 7]) == float:
#         if np.isnan(df.iloc[i, 7]):
#             OrganismID = ""
#         else:
#             OrganismID = str(int(df.iloc[i, 7]))
#     else:
#         OrganismID = df.iloc[i, 7]
#     InteractionDetail = df.iloc[i, 8]
#     Interactions = df.iloc[i, 9].split("|")
#     PubMedIDs = df.iloc[i, 10]
#     for Interaction in Interactions:
#         ChemGeneInteraciton = Relationship(chemical, Interaction, gene, 
#             GeneForms=GeneForms, Organism=Organism, OrganismID=OrganismID, 
#             InteractionDetail=InteractionDetail, PubMedIDs=PubMedIDs)
#         tx.create(ChemGeneInteraciton)

#     if i%CommitQueries==0:
#         graph.commit(tx)
#         tx = graph.begin()
#         toc = time.perf_counter()
#         print(f"Executed {i:d} queries in {toc - tic:0.4f} seconds")

# graph.commit(tx)
toc = time.perf_counter()
print(f"Executed {NumItems:d} queries in {toc - tic:0.4f} seconds")

Result = graph.run("MATCH (n) RETURN count(n)").data()
print(Result)