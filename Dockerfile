FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /mybazar
WORKDIR /mybazar
COPY requirements.txt /mybazar/
RUN pip install -r requirements.txt
RUN pip install docker
COPY . /mybazar/