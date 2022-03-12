from urllib import request
from flask import Flask, render_template, request

from VideoSharing_BL.SchoolService import SchoolService
from VideoSharing_BL.AppSettingsService import AppSettingsService
import VideoSharing_BL.CredentialVerificationService as CredVer
from VideoSharing_BL.UserService import UserService
from VideoSharing_DTO.User import User
from VideoSharing_DTO.School import School
from datetime import datetime

app = Flask(__name__)
classes = ["login", "register", "school_register"]

@app.route('/')
def index():
    #classes = ["Foo","Bar","Baz"]
    
    app_settings_svc = AppSettingsService()

 
    return render_template("index.html",
                            classes=classes,
                            app_name=app_settings_svc.app_name(),
                            app_version=app_settings_svc.app_version())

@app.route('/create_school', methods=['POST'])
def create_school():

    school_name = request.form['schoolName']
    school_state = request.form['schoolState']
    school_city = request.form['schoolCity']
    school_image = request.form['schoolImage']

    school = School()
    school.SchoolName = school_name
    school.SchoolState = school_state
    school.City = school_city
    school.Picture = school_image

    if SchoolService.register_school(school):
        return render_template("schoolname.html", schoolName = school_name)
    
@app.route('/test_form', methods=['POST'])
def test_form():
    #####
    # WE SHOULD SPLIT THIS INTO TWO FUNCTIONS ONE FOR LOGIN AND ONE FOR REGISTER
    #####
    #gets the name and password from the POST payload
    name = request.form['name']
    password = request.form['password']
    user_svc = UserService()
    #choose which error to display
    #must render_template because of route
    user = User()


    if CredVer.validate_password(name, password):        
        user.UserName = name
        user.Pwd = password
        user.LastLogin = datetime.now()
        if user_svc.register(user):
            #if no error go to homepage and register user
            return render_template("name.html",name=name, registered=True)
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

#function to redirect to school register page
@app.route('/school_register')
def school_register():
    return render_template("school_register.html", classes=classes)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
