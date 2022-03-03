FROM python:slim

RUN useradd flaskblog

WORKDIR /home/flaskblog

#COPY requirements.txt requirements.txt
COPY requirements/common.txt requirements/common.txt
COPY requirements/docker.txt requirements/docker.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements/docker.txt
# RUN venv/bin/pip install gunicorn pymysql cryptography

COPY app app
COPY migrations migrations
COPY flaskblog.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP flaskblog.py

RUN chown -R flaskblog:flaskblog ./
USER flaskblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
