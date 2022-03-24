FROM python:3.6.7

WORKDIR usr/src/flask_app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .