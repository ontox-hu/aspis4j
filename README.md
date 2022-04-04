# Ontox4j

## Documentation

* **docs/** - Wiki style documentation  
* **src/**
   * **app.py** - runs the Flask app with GraphiQL for browser
   * **settings.py** - env for Flask and Neo4j (ask for vars.sh)
   * **neo4j_store.py** - Neo4j node/edge CRUD
   * **schema.py** - Graphene GraphQL schema

## Dev
```diff
- Get vars.sh from Tom.
```

Start a virtual environment
```sh
conda create --name ontox4j python=3.8
conda activate ontox4j
pip install -r requirements.txt
```

Or use this nix shell
```sh
nix-shell
```
## Usage

Start the server:

```sh
source vars.sh
python /src/app.py
```

Open a in a browser the GraphiQL interface at http://127.0.0.1:5000/graphql

Example query to read an entity:

```graphql
{
  compound(Id: "3") {
    id
    pubchemCid
    name
  }
}
```

Example query to write an entity:

```graphql
mutation {
  createCompound(name: "Amoxaciline", pubchemCid: "313233") {
    compound {
      name, pubchemCid
    },
    success
  }
}
```
## Troubleshooting

Error message "Cannot connect to any known routers" is related with a Neo4j DB Authentication problem, check your access credentials. 

## Roadmap
1. Get the Neo4j server with GraphiQL working 
2. CDT Chemical Entity
    * Model
    * CRUD
    * Documentation
    * ETL
3. CDT Gene Entity
4. CDT Chemical Gene Interaction
5. Graph Visualization
6. CDT Disease Entity
7. CDT Chemical Disease Association
8. CDT Gene Disease Association
9.  Graph Visualization
10. CDT Pathway Entity
11. CDT Chemical Pathway Association
12. CDT Gene Pathway Association
13. CDT Disease Pathway Association
14. Graph Visualization
