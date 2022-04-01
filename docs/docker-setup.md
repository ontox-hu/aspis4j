# Run neo4j

## Docker-compose
Launches **neo4j** backend and **ontox4j** graphql gateway

```sh
docker-compose up
```
* `localhost:7474/browser` Neo4j browser
* `localhost:5000/graphql` Graphiql API browser

# Standalone Neo4j
Running a neo4j container can help with dev

## Neo4j 
```bash
source vars.sh
docker run -p 7687:7687 -p 7474:7474 \
  -v /data/ontox4j/data:/data \
  -v /data/ontox4j/logs:/logs \
  --env NEO4J_AUTH=${NEO4J_USER}/${NEO4J_PASSWORD} \
  neo4j:latest
```

Now you can connect via

```bash
export NEO4J_HOST="localhost"
python src/app.py
```
