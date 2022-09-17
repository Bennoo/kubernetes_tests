# syntax=docker/dockerfile:1
FROM python:3.9.13-slim-bullseye
RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt