# Neo4j Production DB Installation

```sh
sudo apt update -y && apt upgrade -y
sudo apt install wget openjdk-8-jre gnupg2 apt-transport-https ca-certificates curl software-properties-commo -y
sudo curl -fsSL https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
sudo sudo add-apt-repository "deb https://debian.neo4j.com stable 4.4"
sudo apt install neo4j -y 
```

Install `certbot`

```sh
sudo apt install certbot
```


