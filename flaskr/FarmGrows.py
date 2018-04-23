import pymysql
import json
from flask import request, session, Response
from flaskr import app, db

class FarmGrows():

    @staticmethod
    def add_relation():
        if 'user' in session.keys():
            parsed_json = request.get_json()
            id = parsed_json['id']
            produceName = parsed_json['produceName']

            cursor = db.cursor()
            sql_string = "INSERT INTO FarmGrows (id, produceName) VALUES (" \
                    + id + ", '" + produceName + "')"

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return "Added produce"
        else:
            return "not logged in"

app.add_url_rule('/add_relation', 'add_relation', FarmGrows.add_relation, methods=['POST'])