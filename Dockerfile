FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install python python-pip -y
RUN pip install --upgrade pip
RUN mkdir /opt/app
COPY code/* /opt/app/
RUN pip install -r /opt/app/requirements.txt

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
