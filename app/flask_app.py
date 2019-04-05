# -*- encoding: utf8 -*-

import appengine_config

import logging
import os

from flask import Flask, render_template, request, url_for, make_response, session

app = Flask(__name__)
DEBUG = True
app.debug = True

DEV_ENVIRONMENT = not os.getenv('SERVER_SOFTWARE','').startswith('Google App Engine/')

if DEV_ENVIRONMENT:
    app.logger.warning('We are using a weak secret key')
    app.secret_key = 'my-dummy-secret-key'
else:
    import secret
    app.secret_key = secret.secret_key

app.config.from_object(__name__)


@app.route('/')
def hello():
    handlers = [
        ('Set cookie', url_for('set_cookie')),
        ('Delete cookie', url_for('delete_cookie')),
        ('Insert in session', url_for('create_session')),
        ('Clear session', url_for('clear_session')),
        ]
    return render_template('home.html', handlers=handlers)


@app.route('/set-cookie')
def set_cookie():
    r = make_response()
    r.set_cookie('name', 'Andrea')
    return r


@app.route('/delete-cookie')
def delete_cookie():
    r = make_response()
    r.set_cookie('name', expires = 0)
    return r


@app.route('/create-session')
def create_session():
    session['email'] = 'pinco@pallino.it'
    return 'ok'


@app.route('/clear-session')
def clear_session():
    pass

