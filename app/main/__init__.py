from flask import Flask, Blueprint


mainbp = Blueprint('main', __name__)

from . import views


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    return app