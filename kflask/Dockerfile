FROM python:latest

RUN mkdir /code
COPY dist/ /code/
WORKDIR /code

EXPOSE 5000
CMD python3 -m gunicorn -b 0.0.0.0:5000 kflask.app:app
