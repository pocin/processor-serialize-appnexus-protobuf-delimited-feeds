FROM python:3.6-alpine

WORKDIR /code
RUN apk add --no-cache protobuf && \
    pip install --no-cache-dir --ignore-installed  pytest protobuf https://github.com/keboola/python-docker-application/zipball/master

RUN mkdir -p /data/out/files /data/in/files
COPY . /code/

# Run the application
CMD python3 -u /code/main.py
