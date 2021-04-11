FROM python:3.9.2

RUN apt-get update && apt-get install vim -y

WORKDIR /usr/locust/

COPY requirements.txt /usr/locust/requirements.txt
COPY config.py /usr/locust/config.py
COPY main.py /usr/locust/main.py

ENV VIRTUAL_ENV "/env"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements.txt