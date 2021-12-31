from flask import Flask
from projects.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from projects.routes import view

    app.register_blueprint(view, url_prefix="/")

    return app
