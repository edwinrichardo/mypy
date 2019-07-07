#FROM python:3.6
FROM ubuntu:18.04

COPY . /app

WORKDIR /app

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN pip install --trusted-host --upgrade -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["Main.py"]