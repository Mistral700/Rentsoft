FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

RUN apk update

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /tmp

RUN cd /tmp && pip install -r requirements.txt