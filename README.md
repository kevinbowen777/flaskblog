## Flask Blog

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/flaskblog.svg)](https://github.com/kevinbowen777/flaskblog/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

- A Social Blogging Application

Flask Blog is a demonstration of Flask functionality taken directly from the
exercises in Miguel Grinberg's excellent tutorial [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Installation
Local dev environment:
 - `git clone https://github.com/kevinbowen777/flaskblog.git`
 - `cd flaskblog`
 - `python -m venv venv`
 - `source venv/bin/activate`
 - `pip install -r requirements/dev.txt`
 - `flask run`
 - `flask db upgrade`
   A database named `app.db` will be created with the appropriate tables.
 - Open browser to http://127.0.0.1:5000

Local dev environment(with Docker & MySQL):
 - Download and start a MySQL db:
```
docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=flaskblog -e MYSQL_USER=flaskblog \
    -e MYSQL_PASSWORD=SmQdemoAkZa \
    mysql/mysql-server:latest
```
  - Download and start the flaskblog Docker container:
```
docker run --name microblog -d -p 8000:5000 --rm -e SECRET_KEY=d9dfd9d4db014650428af71c3fd69a47 \
    -e MAIL_SERVER=smtp.googlemail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=user@gmail.example.com -e MAIL_PASSWORD=qnrfblogspksmeta \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://flaskblog:SmQdemoAkZa@dbserver/flaskblog \
    kevinbowen777/flaskblog:latest
```
  - Open browser to http://127.0.0.1:8000
  - NOTE: Be sure to change the credentials used in the commands above. They are
    shown only for example purposes.

## Testing
  - Run unit tests with `python tests.py`

## Features
 - email verification for account registration & password/email change
 - ability to follow specific users
 - filter posts by followed users
 - gravatar support for user icons
 - private messaging between registered users

### Live Application Demo:

TBD

### Docker Container Image:

 - [Flask Blog - Docker Image](https://hub.docker.com/repository/docker/kevinbowen777/flaskblog)

## Screenshots

### Posts
![Posts](images/flaskblog_posts.png)

### Profile
![Profile](images/flaskblog_profile.png)

### Search Results
![Profile](images/flaskblog_search_results.png)

[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/flaskblog/blob/master/LICENSE)

### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/flaskblog/issues)
      to view currently open bug reports or open a new issue.
