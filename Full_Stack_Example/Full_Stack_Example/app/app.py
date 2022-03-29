from operator import truediv
from urllib import request
from flask import Flask, render_template, request, session, abort

from VideoSharing_BL.SchoolService import SchoolService
from VideoSharing_BL.ClassService import ClassService
from VideoSharing_BL.UserSchoolMappingService import USMService
from VideoSharing_BL.AppSettingsService import AppSettingsService
import VideoSharing_BL.CredentialVerificationService as CredVer
from VideoSharing_BL.UserService import UserService
from VideoSharing_DTO.User import User
from VideoSharing_DTO.School import School
from VideoSharing_DTO.Class import Class
from datetime import datetime


app = Flask(__name__)
app.secret_key = "abc"
classes = ["login", "register", "create_school", "create_class"]

@app.route('/')
def index():
    #classes = ["Foo","Bar","Baz"]
    
    app_settings_svc = AppSettingsService()

 
    return render_template("index.html",
                            classes=classes,
                            app_name=app_settings_svc.app_name(),
                            app_version=app_settings_svc.app_version())

@app.route('/create_school_form', methods=['POST'])
def create_school_form():

    school_svc = SchoolService()
    new_school = School()
    new_school.SchoolName = request.form['schoolName']
    new_school.SchoolState = request.form['schoolState']
    new_school.City = request.form['schoolCity']
    new_school.Picture = request.form['schoolImage']

    if school_svc.register_school(new_school):
        return render_template("schoolname.html", school = new_school)
    else:
        exisiting_school = school_svc.get_school(new_school)
        if exisiting_school is not None:
            return render_template("schoolname.html", school = exisiting_school)      
    
@app.route('/create_class_form', methods=['POST'])
def create_class_form():

    class_svc = ClassService()
    new_class = Class()
    new_class.ClassId = request.form['classId']
    new_class.ClassName = request.form['className']
    new_class.ClassCode = request.form['classCode']
    new_class.Section = request.form['section']
    new_class.Semester = request.form['semester']
    new_class.Teacher = request.form['teacher']
    new_class.SchoolId = request.form['schoolId']

    if class_svc.register_class(new_class):
        return render_template("classname.html", cl4ss = new_class)
    else:
        exisiting_class = class_svc.get_class(new_class)
        if exisiting_class is not None:
            return render_template("classname.html", cl4ss = exisiting_class)    

@app.route('/register_form', methods=['POST'])
def register_form():

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
            session['username'] = name # update session variable to keep track of the current user
            return render_template("name.html", classes=classes, name=name, registered=True)
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

@app.route('/join_school_form', methods=['GET', 'POST'])
def join_school_form():
    school_svc = SchoolService()
    user_svc = UserService()
    usm_svc = USMService()

    if not is_user_logged_in():
        return render_template("login.html")
    else:
        school_id = request.form['schoolId']
        user_id = user_svc.get_user(session['username']).UserId

        usm_svc.register_pair(school_id, user_id)

        _school = school_svc.get_school_from_id(school_id)
        return render_template("schoolname.html", school = _school)


@app.route('/login_form', methods=['POST'])
def login_form():
    #check if user existst and password and username match
    #work on login.html
    #finish this function
    #update userrepository so that we can update the users last login timestamp
    #update userservice.py so that it can update the last login
    #check the login function below
    #gets the name and password from the POST payload
    name = request.form['name']
    password = request.form['password']
    user = User()

    user.UserName = name
    user.Pwd = password

    user_svc = UserService()
    #choose which error to display
    #must render_template because of route
    if not user_svc.user_exists(user):
        return render_template("login.html", classes=classes,
                password_error=False, username_error=True)

    if user_svc.check_username_password_match(name, password):     
        user_svc.update_last_login(name)
        session['username'] = name #update session variable in order to keep track of user
        return render_template("name.html",classes=classes, name=name)

    else:
        # raise an error without changing page
        return render_template("login.html", classes=classes,
                password_error=True, username_error=False)

@app.route('/search_form', methods=['POST'])
def search_form():
    search_term = request.form["searchContent"]
    school_svc = SchoolService()
    school_list = school_svc.search_for_schools(search_term)
    return render_template("results.html", schools=school_list)

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
@app.route('/create_school')
def create_school():
    return render_template("create_school.html", classes=classes)

#function to redirect to class register page
@app.route('/create_class')
def create_class():
    return render_template("create_class.html", classes=classes)

def is_user_logged_in() -> bool:
    if 'username' in session:
        return True
    return False

@app.route('/school/<schoolstate>/<schoolcity>/<schoolname>')
def school(schoolstate, schoolcity, schoolname):
    school_svc = SchoolService()
    
    temp_school = School()
    temp_school.SchoolState = schoolstate
    temp_school.City = schoolcity
    temp_school.SchoolName = schoolname

    _school = school_svc.get_school(temp_school)
    if _school is None:
        abort(404)
    return render_template("schoolname.html", school = _school)      
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
