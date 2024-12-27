from flask import Flask

'''
It creates an instance of the flask class
which will be your WSGI application
'''

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World! how are you"

@app.route("/index")
def hello():
    return "Hello, World! This is the index page"

if __name__ == '__main__':
    app.run(debug = True)

