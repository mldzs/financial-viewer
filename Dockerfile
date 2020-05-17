FROM python:3.8.0-alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install -r requirements.txt

COPY . .
