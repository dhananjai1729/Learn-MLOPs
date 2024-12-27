from flask import Flask, render_template

'''
It creates an instance of the flask class
which will be your WSGI application
'''

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>How are you ?</p>
        </body>
    </html>
    """

@app.route("/index")
def hello():
    return render_template("index.html")

@app.route("/Game")
def about():
    return render_template("game.html")

@app.route("/ANN")
def nn():
    return render_template("neural_networks.html")

if __name__ == '__main__':
    app.run(debug = True)

