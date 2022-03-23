# syntax=docker/dockerfile:1
FROM python:3.8

ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y git wget gcc build-essential libssl-dev python-dev postgresql postgresql-contrib nodejs npm

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app/
RUN python manage.py tailwind install --no-input
