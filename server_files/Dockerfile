FROM node:15.14.0

RUN apt-get update && apt-get install vim -y

WORKDIR /usr/src/app

COPY db_example.json /usr/src/app/db.json
COPY package.json /usr/src/app/package.json

RUN npm install -g json-server