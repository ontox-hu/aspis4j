# ontox4j

## Documentation

src/
* **app.py** runs the flask app with graphiql for browser
* **settings.py** env for flask and neo4j (ask for vars.sh)
* **neo4j_store.py**: neo4j node/edge CRUD
* **schema.py**: graphene graphql schema

## Dev
```diff
- Get vars.sh from Tom.
```

Start a virtual environment
```sh
python3.6 -m virtualenv env
source env/bin/activate
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

Open a in a browser the graphiql interface at http://127.0.0.1:5000/graphql

Example query to read an entity:

```json
{
  compound(Id: "3") {
    id
    pubchemCid
    name
  }
}
```

Example query to write an entity:

```json
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
1. Get the graphiql server working 
2. Add ctdbase.org entities (compounds, proteins, etc.)
3. Add ctdbase.org entity relationships
4. Add entity CRUD to graphql schema
5. ETL a pub db (ctdbase, chembl) into ontox4j