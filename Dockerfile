FROM ubuntu:18.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y python3.8 python3-pip

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT ["./entrypoint.sh"]