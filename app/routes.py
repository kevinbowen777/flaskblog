from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kevin'}
    posts = [
        {
            'author': {'username': 'Sophia'},
            'body': 'Beautiful day in Seattle!'
        },
        {
            'author': {'username': 'Marie'},
            'body': 'The movie Casablanca was so romantic!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route'/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
