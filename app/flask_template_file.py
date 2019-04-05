# -*- encoding: utf8 -*-

import appengine_config

import logging

from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True
DEBUG = True

# @app.route('/greeting/<recipient>', methods=['GET', 'POST'])
# def helloworld(recipient):
#     app.logger.debug('Uri parameter:   {}'.format(recipient))
#     app.logger.debug('Uri query:       {}'.format(request.args))
#     app.logger.debug('Request payload: {}'.format(request.data))
#     return render_template('greeting.html', recipient=recipient)

@app.route('/greeting', methods=['GET'])
def greeting_page():
    return render_template('greeting_form.html')

@app.route('/greeting', methods=['POST'])
def greeting_link():
    recipient = request.form['greeting_name']
    return render_template('greeting_link.html', recipient=recipient)