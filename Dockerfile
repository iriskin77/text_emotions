FROM python:3.10-slim

WORKDIR /text_emotions

COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .

EXPOSE 8080

