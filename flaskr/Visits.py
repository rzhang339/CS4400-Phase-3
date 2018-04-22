import pymysql
import json
from flask import request, session, Response
from flaskr import app, db
from datetime import datetime

class Visits():

    @staticmethod
    def add_visit():
        if 'user' in session.keys():
            parsed_json = request.get_json()
            user = session['user']
            email = user['email']
            date = datetime.now()
            rating = parsed_json['rating']
            id = parsed_json['id']

            cursor = db.cursor()
            sql_string = "INSERT INTO Visits (email, date, rating, id) VALUES ('" \
                + email + "', '" \
                + str(date) + "', '" \
                + rating + "', '" \
                + id + "');"
            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return "successfully added visit"
        else:
            return "not logged in"

    @staticmethod
    def get_user_visits():
        if 'user' in session.keys():
            user = session['user']
            email = user['email']

            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = ""

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return_string = json.dumps(cursor.fetchall(), sort_keys=True, indent=4, separators=(',', ': '))
            return return_string  
        else:
            return "not logged in"

    @staticmethod
    def get_property_avg_rating():
        if 'user' in session.keys():
            parsed_json = request.get_json()
            id = parsed_json['id']

            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = ""

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return_string = json.dumps(cursor.fetchall(), sort_keys=True, indent=4, separators=(',', ': '))
            return return_string  
        else:
            return "not logged in"

    @staticmethod
    def get_num_visits():
        if 'user' in session.keys():
            parsed_json = request.get_json()
            id = parsed_json['id']

            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = ""

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return_string = json.dumps(cursor.fetchall(), sort_keys=True, indent=4, separators=(',', ': '))
            return return_string  
        else:
            return "not logged in"


app.add_url_rule('/add_visit', 'add_visit', Visits.add_visit, methods=['POST'])
app.add_url_rule('/get_user_visits', 'get_user_visits', Visits.get_user_visits, methods=['GET'])
app.add_url_rule('/get_property_avg_rating', 'add_visit', Visits.add_visit, methods=['POST'])
app.add_url_rule('/get_num_visits', 'get_num_visits', Visits.get_num_visits, methods=['POST'])
