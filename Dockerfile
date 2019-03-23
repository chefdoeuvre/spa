FROM debian
MAINTAINER chefdoeuvre
RUN mkdir /etc/baseapp
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install python python-flask -y
EXPOSE 5000
ENTRYPOINT "python /etc/baseapp/start.py"