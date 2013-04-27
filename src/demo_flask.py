'''
Created on 2013-4-27

@author: EYE
'''

from flask import Flask
from flask import render_template
from jinja2 import Template

app = Flask(__name__)

template = Template('Hello {{ name }}!')

@app.route('/')
def hello_world():
    return template.render(name = 'Gaojie')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/ble/')
def ble(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(None, None, True)
    



