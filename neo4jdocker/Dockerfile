FROM ubuntu:20.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install wget -y
RUN apt-get install openjdk-8-jre -y
RUN apt-get install -y gnupg2
RUN wget -O - https://debian.neo4j.com/neotechnology.gpg.key | apt-key add -
RUN echo 'deb https://debian.neo4j.com stable 4.4' | tee /etc/apt/sources.list.d/neo4j.list
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y neo4j 

WORKDIR /

COPY . /

EXPOSE 7687
EXPOSE 7474

CMD service neo4j restart && tail -F /var/log/neo4j/neo4j.log
