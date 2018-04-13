from . import article_bp as article
from flask import render_template


@article.route('/')
def index():
    return render_template('articles/index.html')


@article.route('/new')
def new():
    return render_template('articles/new.html')