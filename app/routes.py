from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kevin'}
    return '''
<html>
    <head>
        <title>Home Page - Flaskblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
