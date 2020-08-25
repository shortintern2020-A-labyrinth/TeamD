FROM python:buster

RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . .

CMD ["python", "./manage.py", "runserver 0.0.0.0:8000"]
