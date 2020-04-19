FROM python:3.7

MAINTAINER IbrahimSY

ADD . /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update

RUN apt-get install python3-dev default-libmysqlclient-dev  -y

#RUN curl https://dl.fbaipublicfiles.com/fairseq/models/wmt14.v2.en-fr.fconv-py.tar.bz2 | tar xvjf - -C ./blog/language

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD gunicorn -b :80 myblog.wsgi

