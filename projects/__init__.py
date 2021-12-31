from projects import routes
from flask import Flask
from projects.config import Config


app = Flask(__name__)
app.config.from_object(Config)
