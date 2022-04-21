import random
from random import randint

from faker import Faker
from sqlalchemy.exc import IntegrityError

from app import db

from .models import Post, User


def users(count=100):
    fake = Faker()
    i = 0
    while i < count:
        u = User(
            email=fake.email(),
            username=fake.user_name(),
            password_hash="password",
            about_me=fake.text(),
            last_seen=fake.past_date(),
        )
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()


def posts(count=100):
    fake = Faker()
    # user_count = User.query.count()
    # user_count = 104
    for i in range(count):
        guess = 100
        # u = User.query.offset(randint(0, user_count - 1)).first()
        u = User.query.offset(guess).first()
        p = Post(body=fake.text(), timestamp=fake.past_date(), user_id=u)
        db.session.add(p)
        guess -= 1
    db.session.commit()
