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
	return render_template('Login.html')

@app.route('/homescreen_owner')
def homescreen_owner():
	if (session['user']['userType'] == "owner"):
		return render_template('HomescreenOwner.html')
	else:
		return "Invalid credentials"

@app.route('/homescreen_visitor')
def homescreen_visitor():
	if (session['user']['userType'] == "visitor"):
		return render_template('HomescreenVisitor.html')
	else:
		return "Invalid credentials"

@app.route('/homescreen_admin')
def homescreen_admin():
	if (session['user']['userType'] == "admin"):
		return render_template('HomescreenAdmin.html')
	else:
		return "Invalid credentials"

if __name__ == '__main__':
	app.run()