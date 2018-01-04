FROM python:3.6-slim

# Initialize
RUN mkdir -p /data/web
WORKDIR /data/web

# Prepare
COPY . /data/web/

# Setup
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt