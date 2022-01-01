from projects.forms import LoginForm
from flask import render_template, Blueprint
from projects.forms import LoginForm

view = Blueprint('view', __name__)


@view.route('/')
@view.route('/home')
def home():
    return render_template('home.html', title="Home")


@view.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In')


@view.route('/users')
def users():
    return render_template('users.html')


@view.route('/barang')
def barang():
    return render_template('barang.html')
