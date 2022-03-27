# syntax=docker/dockerfile:1
FROM python:3.8

ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y \
    nodejs npm \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/

WORKDIR /app
RUN useradd -m webapp \
    && chown -R webapp /app

USER webapp
COPY --chown=webapp requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY --chown=webapp . /app/
RUN python manage.py tailwind install --no-input
