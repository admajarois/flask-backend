from projects.forms import LoginForm
from flask import render_template
from projects import app
from projects.forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In')

@app.route('/users')
def users():

    return render_template('users.html')
