from urllib import request
from flask import Flask, render_template, request

from VideoSharing_BL.AppSettingsService import AppSettingsService
from VideoSharing_BL.UserService import UserService
from VideoSharing_DTO.User import User

app = Flask(__name__)

@app.route('/')
def index():
    classes = ["Foo","Bar","Baz"]

    app_settings_svc = AppSettingsService()

 
    return render_template("index.html",
                            classes=classes,
                            app_name=app_settings_svc.app_name(),
                            app_version=app_settings_svc.app_version())

@app.route('/test_form', methods=['POST'])
def test_form():
    name = request.form['name']
    user_svc = UserService()

    user = User()
    user.UserName = name
    
    retVal = user_svc.register(user)

    return render_template("name.html",name=name, registered=retVal)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
