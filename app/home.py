# -*- encoding: utf8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)
DEBUG = True

@app.route('/home', methods=['GET', 'POST'])
def hello():
	return render_template('home.html')

