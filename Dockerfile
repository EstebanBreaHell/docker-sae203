FROM debian:latest

RUN apt update -y \
    && apt upgrade -y \
    && apt install python3-pip -y

ADD . /sae203

WORKDIR /sae203

RUN pip3 install -r requirements.txt



CMD ["uwsgi", "--socket", "0.0.0.0:80", "--protocol=http", "-w", "wsgi:app"]