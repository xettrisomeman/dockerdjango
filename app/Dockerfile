FROM python:3-alpine 

WORKDIR /app


ENV PYTHONDONTWRITEBYTECODES 1

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app



