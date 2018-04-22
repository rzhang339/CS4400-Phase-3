from flask import Flask, render_template
from flask import request

import User
import Property
import Produce
import Visits
import FarmGrows

from flaskr import app

@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response

@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

@app.route('/')
def index():
	return render_template('Login.html')

@app.route('/homescreen_owner')
def homescreen_owner():
	return render_template('HomescreenOwner.html')

if __name__ == '__main__':
	app.run()