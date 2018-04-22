from flask import Flask, render_template, session
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
	if 'user' not in session.keys():
		return render_template('Login.html')
	elif session['user']['userType'] == 'admin':
		return render_template('HomescreenAdmin.html')
	elif session['user']['userType'] == 'owner':
		return render_template('HomescreenOwner.html')
	elif session['user']['userType'] == 'visitor':
		return render_template('HomescreenVisitor.html')
	else:
		return "Invalid Credentials"

@app.route('/register/owner')
def register_owner():
	return render_template('OwnerRegistration.html')

@app.route('/register/visitor')
def register_visitor():
	return render_template('VisitorRegistration.html')

if __name__ == '__main__':
	app.run()