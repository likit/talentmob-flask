from flask import Flask, Blueprint


mainbp = Blueprint('main', __name__)

from . import views