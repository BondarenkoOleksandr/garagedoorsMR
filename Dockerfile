FROM python:3.8

RUN apt update

COPY ./commands ./commands
RUN chmod u+x ./commands/start_server.sh
RUN chmod u+x ./commands/start_nginx.sh

RUN mkdir /srv/project
WORKDIR /srv/project

COPY ./src ./src
COPY src/requirements.txt ./requirements.txt

RUN pip install -r requirements.txt


CMD ["bash"]
