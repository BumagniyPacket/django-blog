FROM python:3
RUN mkdir blog-project
WORKDIR /blog-project
ADD requirements.txt /blog-project/
RUN pip install -r requirements.txt
ADD . /blog-project/
