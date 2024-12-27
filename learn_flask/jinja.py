### Building Url dynamically
## Variable Rule
### Jinja 2 Template Engine

from flask import Flask,render_template,request
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res = ''
    if int(score) > 50:
        res = 'Congratulations!'
    else:
        res = 'Sorry, you failed.'
    exp = {"score":score,"result":res}

    return render_template('result1.html', results=exp)


@app.route('/successif/<int:score>')
def successif(score):
    res = ''
    if int(score) > 50:
        res = 'Congratulations!'
    else:
        res = 'Sorry, you failed.'
    exp = {"score":score,"result":res}

    return render_template('result1.html', results=exp)

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


if __name__=="__main__":
    app.run(debug=True)
