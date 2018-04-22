import pymysql
import json
from flask import request, session, Response
from flaskr import app, db

class Produce():

    @staticmethod
    def add_produce():
        if 'user' in session.keys():
            parsed_json = request.get_json()
            name = parsed_json['name']
            type = parsed_json['type']

            cursor = db.cursor()
            sql_string = "INSERT INTO Produce (produceName, produceType) VALUES ('" \
                    + name + "', '" + type + "')"

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return "Added produce"
        else:
            return "not logged in"

    @staticmethod
    def delete_produce():
        if 'user' in session.keys():
            parsed_json = request.get_json()
            name = parsed_json['name']

            cursor = db.cursor()
            sql_string = "DELETE from Produce WHERE produceName = '" + name + "'"

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return "Deleted produce"
        else:
            return "not logged in"

    @staticmethod
    def approve_produce():
        if 'user' in session.keys():
            parsed_json = request.get_json()
            name = parsed_json['name']

            cursor = db.cursor()
            sql_string = "UPDATE Produce SET itemApproved = 1 where produceName = '" + name + "'"  

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return "approved"
        else:
            return "not logged in"

    @staticmethod
    def get_unapproved_produce():
        if 'user' in session.keys():
            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = "SELECT produceName, produceType from Produce WHERE itemApproved = 0"  

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
    def get_approved_produce():
        if 'user' in session.keys():
            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = "SELECT produceName, produceType from Produce WHERE itemApproved = 1"  

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
    def get_farm_animals():
        if 'user' in session.keys():
            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = "SELECT produceName FROM Produce WHERE produceType = 'animal' ORDER BY produceName ASC;"

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
    def get_farm_crops():
        if 'user' in session.keys():
            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = "SELECT produceName FROM Produce WHERE produceType = 'fruit' OR produceType = 'nut' OR produceType = 'vegetable' OR produceType = 'flower' ORDER BY produceName ASC;"

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
    def get_garden_crops():
        if 'user' in session.keys():
            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = "SELECT produceName FROM Produce WHERE produceType = 'vegetable' OR produceType = 'flower' ORDER BY produceName ASC;"

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
    def get_orchard_crops():
        if 'user' in session.keys():
            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = "SELECT produceName FROM Produce WHERE produceType = 'fruit' OR produceType = 'nut' ORDER BY produceName ASC;"

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return_string = json.dumps(cursor.fetchall(), sort_keys=True, indent=4, separators=(',', ': '))
            return return_string
        else:
            return "not logged in"



app.add_url_rule('/add_produce', 'add_produce', Produce.add_produce, methods=['POST'])
app.add_url_rule('/delete_produce', 'delete_produce', Produce.delete_produce, methods=['POST'])
app.add_url_rule('/approve_produce', 'approve_produce', Produce.approve_produce, methods=['POST'])
app.add_url_rule('/get_unapproved_produce', 'get_unapproved_produce', Produce.get_unapproved_produce, methods=['GET'])
app.add_url_rule('/get_approved_produce', 'get_approved_produce', Produce.get_approved_produce, methods=['GET'])
app.add_url_rule('/get_farm_animals', 'get_farm_animals', Produce.get_farm_animals, methods=['GET'])
app.add_url_rule('/get_farm_crops', 'get_farm_crops', Produce.get_farm_crops, methods=['GET'])
app.add_url_rule('/get_garden_crops', 'get_garden_crops', Produce.get_garden_crops, methods=['GET'])
app.add_url_rule('/get_orchard_crops', 'get_orchard_crops', Produce.get_orchard_crops, methods=['GET'])


