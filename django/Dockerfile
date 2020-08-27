FROM python:buster

ENV PORT 8000
EXPOSE 8000
RUN apt-get update

RUN apt-get install -y libgl1-mesa-glx libx264-dev \
    ffmpeg nasm yasm libmp3lame-dev \ 
    libopus-dev libvorbis-dev libvpx-dev

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . .
# RUN bash install-ffmpeg.sh

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
