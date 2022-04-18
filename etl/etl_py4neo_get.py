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

Result = graph.run("MATCH (n:Chemical) RETURN count(n)").data()
print(str(Result[0].get("count(n)")) + " Chemicals")
Result = graph.run("MATCH (n:Gene) RETURN count(n)").data()
print(str(Result[0].get("count(n)")) + " Genes")
Result = graph.run("MATCH (n) RETURN count(n)").data()
print(str(Result[0].get("count(n)")) + " Total items")
Result = graph.run("MATCH (x)-[ix]->(y) RETURN count(ix)").data()
print(str(Result[0].get("count(ix)")) + " Total relationships")
