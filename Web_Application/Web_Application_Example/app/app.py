from urllib import request
from flask import Flask, render_template, request
app = Flask(__name__)
classes = ["login", "register"]


@app.route('/')
def index():
    return render_template("index.html",classes=classes)

@app.route('/test_form', methods=['POST'])
def test_form():
    #gets the name and password from the POST payload
    name = request.form['name']
    password = request.form['password']
    return render_template("name.html",name=name, password=password)

#function to redirect to register page
@app.route('/register')
def register():
    return render_template("register.html",classes=classes)

#function to redirect to login page
@app.route('/login')
def login():
    return render_template("login.html", classes=classes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
