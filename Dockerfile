FROM python:slim

RUN useradd flaskblog

WORKDIR /home/flaskblog

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql cryptography

COPY app app
COPY migrations migrations
COPY flaskblog.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP flaskblog.py

RUN chown -R flaskblog:flaskblog ./
USER flaskblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
