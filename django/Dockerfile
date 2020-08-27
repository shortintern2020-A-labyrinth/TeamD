FROM python:buster

RUN apt-get update

RUN apt-get install libgl1-mesa-glx
RUN apt-get install libx264-dev
RUN apt-get install -y ffmpeg

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code

RUN bash install-ffmpeg.sh

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . .
