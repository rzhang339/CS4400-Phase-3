import pymysql
import json
from flask import request, session, Response
from flaskr import app, db

class Produce():

    @staticmethod
    def add_produce():
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

    

app.add_url_rule('/add_produce', 'add_produce', Produce.add_produce, methods=['POST'])