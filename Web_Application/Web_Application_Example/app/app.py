from urllib import request
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    classes = ["Foo","Bar","Baz"]
    return render_template("index.html",classes=classes)

@app.route('/test_form', methods=['POST'])
def test_form():
    name = request.form['name']
    return render_template("name.html",name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
