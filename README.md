# Ontox4j

## Documentation

src/
* **app.py** runs the Flask app with GraphiQL for browser
* **settings.py** env for Flask and Neo4j (ask for vars.sh)
* **neo4j_store.py**: Neo4j node/edge CRUD
* **schema.py**: Graphene GraphQL schema

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


## Roadmap
1. [x] Get the Neo4j server with GraphiQL working 
2. [ ] Add CTD (Comparative Toxicogenomics Database) entities
   1.  Chemical
   2.  Gene
   3.  Disease
   4.  Pathway
3. [ ] Add CDT entity relationships
4. [ ] Add entity CRUD to graphql schema
5. [ ] ETL a pub db (ctdbase, chembl) into ontox4j