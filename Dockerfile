# FROM python:3
# ENV PYTHONUNBUFFERED 1
# WORKDIR /app
# COPY requirements.txt /app/requirements.txt
# RUN pip install -r requirements.txt
# COPY . /app/

# CMD python manage.py runserver 0.0.0.0:8000

FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
