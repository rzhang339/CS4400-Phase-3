import pymysql
from flask import Flask
from flask_cors import CORS, cross_origin

db = pymysql.connect(host = 'academic-mysql.cc.gatech.edu',
								user = 'cs4400_team_34',
								password = 'stdT4YpR',
								db = 'cs4400_team_34')
app = Flask('CS4400')
app.config['SECRET_KEY'] = 'Zwo81Qe3Pi7aAHnsPVGkjyW2FApg9ekJVN26iWPRps4='
CORS(app)


def test():
	return "test"

app.add_url_rule('/test', 'test', test, methods=['GET'])

