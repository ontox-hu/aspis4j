# Neo4j Migration from Community to Enterprise

Remove Neo4j Community installation
```sh
service neo4j stop
neo4j-admin dump --database=neo4j --to=/mnt/md0/202204280834_neo4j.dump --verbose
sudo cp /etc/neo4j/neo4j.conf /mnt/md0/202204280834_neo4j.conf
sudo cp /etc/neo4j/apoc.conf /mnt/md0/202204280834_apoc.conf
sudo apt-get remove neo4j
```

Remove remaining folders
```sh
sudo rm -r /etc/neo4j
sudo rm -r /var/lib/neo4j
```

Install Neo4j Enterprise
```sh
sudo apt-get install neo4j-enterprise
service neo4j status
service neo4j start
```

Set a secure password
```sh
cypher-shell -u neo4j -p neo4j
```

Restore Neo4j config file
```sh
sudo cp /mnt/md0/202204280834_neo4j.conf /etc/neo4j/neo4j.conf
```

Restore certificates
```sh
export NEO4JSSL=/var/lib/neo4j/certificates
sudo mkdir $NEO4JSSL/bolt
sudo mkdir $NEO4JSSL/bolt/trusted
sudo mkdir $NEO4JSSL/bolt/revoked
sudo mkdir $NEO4JSSL/https
sudo mkdir $NEO4JSSL/https/trusted
sudo mkdir $NEO4JSSL/https/revoked
export DOMAIN=aspis4j.com
cd $NEO4JSSL
sudo ln -s /etc/letsencrypt/live/$DOMAIN/fullchain.pem bolt/public.crt
sudo ln -s /etc/letsencrypt/live/$DOMAIN/fullchain.pem bolt/trusted/public.crt
sudo ln -s /etc/letsencrypt/live/$DOMAIN/privkey.pem bolt/private.key
sudo ln -s /etc/letsencrypt/live/$DOMAIN/fullchain.pem https/public.crt
sudo ln -s /etc/letsencrypt/live/$DOMAIN/fullchain.pem https/trusted/public.crt
sudo ln -s /etc/letsencrypt/live/$DOMAIN/privkey.pem https/private.key
sudo chgrp -R neo4j *
sudo chmod -R g+rx *
```

Restart Neo4j service
```sh
service neo4j restart
```

Check new configuration
```sh
source vars.sh
cypher-shell -d system -a neo4j+s://aspis4j.com:7687
neo4j@system> SHOW DATABASES;
```

Install APOC
```sh
sudo cp /mnt/md0/202204280834_apoc.conf /etc/neo4j/apoc.conf
sudo wget https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/4.4.0.1/apoc-4.4.0.1-all.jar
service neo4j restart
```

Check APOC
```sh
cypher-shell -a neo4j+s://aspis4j.com:7687
neo4j@neo4j> RETURN apoc.version();
```

Restore database
```sh
service neo4j stop
neo4j-admin load --from=/mnt/md0/202204280834_neo4j.dump --database=neo4j --force --verbose
sudo chown -R neo4j:neo4j /var/lib/neo4j
service neo4j start
```
