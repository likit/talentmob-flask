from . import mainbp as main

@main.route('/')
def index():
    return '<h1>Hello, Main page!</h1>'