from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Erik'}
    return render_template('index.html', title='Home', user=user, app_name="Game Time")
