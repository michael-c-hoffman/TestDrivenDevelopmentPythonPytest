FROM python:latest

RUN mkdir /code
COPY dist/ /code/
WORKDIR /code

EXPOSE 5000
CMD python3 -m kflask
