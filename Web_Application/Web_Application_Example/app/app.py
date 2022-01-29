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
    #choose which error to display
    #must render_template because of route
    if validate_password(name, password):
        if validate_username(name):
            #if no error go to homepage
            return render_template("name.html",name=name, password=password)
        else:
            password_error = False
            username_error = True
            return render_template("register.html", classes=classes,password_error=password_error,
                                    username_error=username_error)
    else:
        password_error = True
        username_error = False
        # raise an error without changing page
        return render_template("register.html", classes=classes,password_error=password_error,
                                    username_error=username_error)

#function to redirect to register page
@app.route('/register')
def register():
    password_error = False
    username_error = False    
    return render_template("register.html", classes=classes,password_error=password_error,
                                    username_error=username_error)
#function to redirect to login page
@app.route('/login')
def login():
    return render_template("login.html", classes=classes)

def validate_username(name):
    return True

def validate_password(name: str, pwd: str) -> bool:
    
    #Return False if the substring of the username is in the string password
    #Return False if the length of the password is less than 8
    #if there is no number in the string return false
    #If the number of unique characters in the string is fewer than 4 return False
    if name in pwd:
        return False
    if len(pwd) < 8:
        return False
    if not number_in_string(pwd):
        return False
    if len(set(pwd))< 4:
        return False
    return True



def number_in_string(string: str) -> bool:
    #Converts The string into a list, then keeps only the numbers in the string and makes a new list
    #If the length of the string with the numbers is less than one then there are no numbers in the string
    number_list = [x for x in list(string) if x.isdigit()]
    if len(number_list) < 1:
        return False
    return True


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
