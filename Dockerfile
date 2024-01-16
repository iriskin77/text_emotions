FROM python:3.10-slim

WORKDIR /text_emotions

COPY . /text_emotions
RUN pip install -r requirements.txt

EXPOSE 8080

