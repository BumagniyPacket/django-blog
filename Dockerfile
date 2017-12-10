FROM python:3
RUN mkdir
WORKDIR /blog
ADD requirements.txt /blog/
RUN pip install -r requirements.txt
ADD . /blog/
