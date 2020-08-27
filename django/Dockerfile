FROM python:buster

ENV PORT 8000
EXPOSE 8000
RUN apt-get update

RUN apt-get install -y libgl1-mesa-glx
RUN apt-get install -y libx264-dev
RUN apt-get install -y ffmpeg
RUN apt-get install -y nasm
RUN apt-get install -y libmp3lame-dev

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . .

RUN chmod +x ./install-ffmpeg.sh
RUN ["/bin/bash", "-c", "./install-ffmpeg.sh"]

# CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
