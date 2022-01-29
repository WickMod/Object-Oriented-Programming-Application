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
    if validate_password() and validate_username():
        return render_template("name.html",name=name, password=password)
    else:
        # raise an error without changing page
        pass

#function to redirect to register page
@app.route('/register')
def register():
    return render_template("register.html",classes=classes)

#function to redirect to login page
@app.route('/login')
def login():
    return render_template("login.html", classes=classes)

def validate_password(name):
    return True

def validate_username(password):
    return True


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
