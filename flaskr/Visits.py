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
                + str(date) + "', " \
                + rating + ", " \
                + id + ");"
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
            sql_string = "SELECT propertyName, date, rating FROM Visits JOIN Property" \
                    + " ON Visits.id = Property.id WHERE Visits.email = '" \
                    + email + "';"

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            visits = cursor.fetchall()
            list = []
            for visit in visits:
                print (visit)
                dict = {
                    "propertyName": visit['propertyName'],
                    "date": str(visit['date']),
                    "rating": visit['rating']
                }
                list.append(dict)
            return_string = json.dumps(list, sort_keys=True, indent=4, separators=(',', ': '))
            return return_string
        else:
            return "not logged in"

    @staticmethod
    def remove_visit():
        if 'user' in session.keys():
            user = session['user']
            parsed_json = request.get_json()
            username = user['username']
            id = parsed_json['id']

            cursor = db.cursor()
            sql_string = "DELETE FROM Visits WHERE id = '" + id + "' AND username = '" + username + "';"
            print (sql_string)
            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return "deleted"
        else:
            return "not logged in"

    @staticmethod
    def remove_all_visits():
        if 'user' in session.keys():
            #user = session['user']
            parsed_json = request.get_json()
            username = parsed_json['username']
            print (username)
            #id = parsed_json['id']

            cursor = db.cursor()
            sql_string = "DELETE FROM Visits WHERE username = '" + username + "';"
            print (sql_string)
            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return "deleted"
        else:
            return "not logged in"

    @staticmethod
    def get_visitors():
        if 'user' in session.keys():
            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = "select User.username, email, count(id) as visitCount "\
            + "from User left join Visits on User.username = Visits.username "\
            + "where userType = 'visitor' Group by Visits.username;"
            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            visits = cursor.fetchall()
            list = []
            for visit in visits:
                print (visit)
                dict = {
                "username": visit['username'],
                "email": visit['email'],
                "visitCount": visit['visitCount']
                }
                list.append(dict)
            return_string = json.dumps(list, sort_keys=True, indent=4, separators=(',', ': '))
            print (return_string)
            return return_string
        else:
            return "not logged in"

    @staticmethod
    def remove_visitor():
        if 'user' in session.keys():
            #user = session['user']
            parsed_json = request.get_json()
            username = parsed_json['username']
            print (username)
            #id = parsed_json['id']

            cursor = db.cursor()
            sql_string = "DELETE FROM User WHERE username = '" + username + "';"
            print (sql_string)
            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return "deleted"
        else:
            return "not logged in"


app.add_url_rule('/add_visit', 'add_visit', Visits.add_visit, methods=['POST'])
app.add_url_rule('/get_user_visits', 'get_user_visits', Visits.get_user_visits, methods=['GET'])
app.add_url_rule('/remove_visit', 'remove_visit', Visits.remove_visit, methods=['POST'])
app.add_url_rule('/get_visitors', 'get_visitors', Visits.get_visitors, methods=['GET'])
app.add_url_rule('/remove_all_visits', 'remove_all_visits', Visits.remove_all_visits, methods=['POST'])
app.add_url_rule('/remove_visitor', 'remove_visitor', Visits.remove_visitor, methods=['POST'])
