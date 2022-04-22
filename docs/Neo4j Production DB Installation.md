# Neo4j Production DB Installation

Install `certbot`

```sh
sudo apt install certbot
```

Modify default password running `cypher-shell`

Certificate folder structure
```sh
export NEO4JSSL=/var/lib/neo4j/certificates
sudo mkdir $NEO4JSSL/bolt
sudo mkdir $NEO4JSSL/bolt/trusted
sudo mkdir $NEO4JSSL/bolt/revoked
sudo mkdir $NEO4JSSL/https
sudo mkdir $NEO4JSSL/https/trusted
sudo mkdir $NEO4JSSL/https/revoked
```

Create symbolic links to certificates
```sh
export DOMAIN=aspis4j.com
cd $NEO4JSSL
sudo ln -s /etc/letsencrypt/live/$DOMAIN/fullchain.pem bolt/public.crt
sudo ln -s /etc/letsencrypt/live/$DOMAIN/fullchain.pem bolt/trusted/public.crt
sudo ln -s /etc/letsencrypt/live/$DOMAIN/privkey.pem bolt/private.key
sudo ln -s /etc/letsencrypt/live/$DOMAIN/fullchain.pem https/public.crt
sudo ln -s /etc/letsencrypt/live/$DOMAIN/fullchain.pem https/trusted/public.crt
sudo ln -s /etc/letsencrypt/live/$DOMAIN/privkey.pem https/private.key
```

Make everything readable to the DB
```sh
sudo chgrp -R neo4j *
sudo chmod -R g+rx *
```

Add following lines to `/etc/neo4j/neo4j.conf`
```sh
dbms.default_listen_address=0.0.0.0
dbms.default_advertised_address=aspis4j.com
dbms.ssl.policy.bolt.enabled=true
dbms.ssl.policy.bolt.base_directory=certificates/bolt
dbms.ssl.policy.bolt.private_key=private.key
dbms.ssl.policy.bolt.public_certificate=public.crt
dbms.ssl.policy.bolt.client_auth=NONE
```

Restart Neo4j service
```sh
service neo4j restart
```

# Install APOC procedures

Download lastest release of APOC in Neo4j plugins folder. Version of APOC and Neo4j should match.

```sh
cd /var/lib/neo4j/plugins
sudo wget https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/4.4.0.1/apoc-4.4.0.1-all.jar
```

Add following lines to `/etc/neo4j/neo4j.conf`
```sh
dbms.security.procedures.unrestricted=apoc.*
```

Create a file `/etc/neo4j/apoc.conf` with the following line
```sh
apoc.import.file.enabled=true
```


Restart Neo4j service
```sh
service neo4j restart
```

Check installation
```sh
export NEO4J_USERNAME=neo4j
export NEO4J_PASSWORD=
cypher-shell -a neo4j+s://aspis4j.com:7687
```

In the cypher shell
```
neo4j@neo4j> RETURN apoc.version();
``` 

and the answer should be
```
+----------------+
| apoc.version() |
+----------------+
| "4.4.0.1"      |
+----------------+

1 row
ready to start consuming query after 2 ms, results consumed after another 0 ms
```

# Neo4j Migrations

Follow the Neo4j Migrations Doc and change the address in `.migrations.properties``
```sh
address=bolt+s\://aspis4j.com\:7687
```

 # ETL CTD 

The file `ETL_CTD.sh` download the file from CTD, decrompess and remove the first 29 lines of header.

```sh
sudo ./ETL_CTD.sh
```

Perform Neo4j Migrations

Nodes
     175100 CTD_chemicals.csv
     564848 CTD_genes.csv
      13178 CTD_diseases.csv
       2567 CTD_pathways.csv

Realtionships
     135783 CTD_genes_pathways.csv
     599734 CTD_diseases_pathways.csv 294s
    2346085 CTD_chem_gene_ixns.csv 
            313829 14:39
            346550 14:53
    7854278 CTD_chemicals_diseases.csv
   94153736 CTD_genes_diseases.csv


