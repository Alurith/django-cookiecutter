# syntax=docker/dockerfile:1
FROM python:3.8-alpine3.15 as build
ENV PYTHONUNBUFFERED=1 \
    PATH="/usr/app/venv/bin:$PATH"

WORKDIR /usr/app

RUN apk update && apk add --no-cache \
    gcc libpq-dev libc-dev \
    nodejs npm

RUN python -m venv /usr/app/venv
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

FROM build as develop
WORKDIR /app
COPY . /app/

RUN python manage.py tailwind install --no-input
