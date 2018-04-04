from . import main

@main.route('/',methods = ['POST','GET'])
def index():
    return '<h1>Hello world<h1>'