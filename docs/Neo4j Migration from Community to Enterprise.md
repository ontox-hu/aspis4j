# Neo4j Migration from Community to Enterprise

```sh
service neo4j stop
neo4j-admin dump --database=neo4j --to=/mnt/md0/202204280834_neo4j.dump --verbose
sudo cp /etc/neo4j/neo4j.conf /mnt/md0/202204280834_neo4j.conf
sudo cp /etc/neo4j/apoc.conf /mnt/md0/202204280834_apoc.conf
sudo apt-get remove neo4j
sudo apt-get install neo4j-enterprise
```