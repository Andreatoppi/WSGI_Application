# -*- encoding: utf8 -*-

import appengine_config

from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True
DEBUG = True

@app.route('/', methods=['GET', 'POST'])
def helloworld():
    return render_template('hello_world.html')

