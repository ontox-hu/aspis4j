from doctest import DocFileCase
import requests
import pandas as pd
import numpy as np
import json
import time
import py2neo

def run_query(uri, query, statusCode, headers):
    request = requests.post(uri, json={'query': query}, headers=headers)
    if request.status_code == statusCode:
        return request.json()
    else:
        raise Exception(f"Unexpected status code returned: {request.status_code}")

def create_query(ChemicalName, ChemicalID, CasRN):
    return ("mutation { createChemical(ChemicalName: \"" + ChemicalName + 
    "\", ChemicalID: \"" + ChemicalID + "\", CasRN: \"" + CasRN +  
    "\") {chemical { ChemicalName ChemicalID CasRN } success } }")

URI = 'http://127.0.0.1:5000/graphql'
Token = 'string'
Headers = {"Authorization": "Bearer " + Token}
StatusCode = 200

Query1 = """
{
  chemicals {
    ChemicalID
    CasRN
  }
}
"""

Query2 = """
mutation {
  createChemical(ChemicalName: "Acetaminophen", ChemicalID: "D000082", CasRN: "103-90-2") {
    chemical {
      ChemicalName
      ChemicalID
      CasRN
    }
    success
  }
}
"""

Query3 = """
mutation {
  deleteChemical(ChemicalID: "D000082") {
    success
  }
}
"""

df = pd.read_csv('./CTDChemicals003.csv', skiprows=27)
df.rename(columns = {'# ChemicalName':'ChemicalName'}, inplace = True)
df.drop([0], inplace = True)
NumItems = len(df.index)

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
    Query = create_query(ChemicalName, ChemicalID, CasRN)
    result = run_query(URI, Query, StatusCode, Headers)
    result_success = result['data']['createChemical']['success']
    if result_success!=True: 
        print("Error in index: " + str(i))
toc = time.perf_counter()
print(f"Executed {NumItems:d} queries in {toc - tic:0.4f} seconds")

#result = run_query(URI, Query1, StatusCode, Headers)
#print(result)

#sg = py2neo.SystemGraph("neo4j+s://3cdad3ee.databases.neo4j.io:7687", auth=("neo4j", "KA8OWOLlBLckFrV_oqmPrQvCs-XkXEzf2PB7JuQfE40"))
#sg.call("dbms.security.listUsers")

graph = py2neo.Graph("neo4j+s://c61a7d98.databases.neo4j.io:7687", auth=("neo4j", "yY6Zqq_j2Y_6UjtGXidKjD_DjQUP1FQ04DEfWabB3j4"))
Result = graph.run("MATCH (n) RETURN n").data()
print(Result)