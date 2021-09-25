from flask import Flask
from projects.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from projects import routes