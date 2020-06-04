FROM python:3.7-slim

RUN apt-get update \ 
    && apt-get install --yes --no-install-recommends \
    wget \
    vim


COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY app /app
WORKDIR /app
CMD python main.py