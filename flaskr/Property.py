import pymysql
import json
import uuid
from flask import request, session, Response
from flaskr import app, db

class Property():

    @staticmethod
    def add_property():
        if 'user' in session.keys():
            parsed_json = request.get_json()
            propertyName = parsed_json['propertyName']
            isPublic = parsed_json['isPublic']
            size = parsed_json['size']
            isCommercial = parsed_json['isCommercial']
            streetAddress = parsed_json['streetAddress']
            city = parsed_json['city']
            zip = parsed_json['zip']
            propertyType = parsed_json['propertyType']
            ownedBy = parsed_json['ownedBy']

            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = "SELECT MAX(id) FROM Property"
            cursor.execute(sql_string)

            max_id = cursor.fetchone()
            if max_id is None or max_id['MAX(id)'] is None:
                id = "0"
            else:
                id  = str(int(max_id['MAX(id)']) + 1)

            sql_string = "INSERT INTO Property (propertyName, id, isPublic, size, isCommercial, streetAddress, city, zip, propertyType, ownedBy) VALUES ('" \
                    + propertyName + "', '" + id + "', '" + isPublic + "', '" \
                    + size + "', '" + isCommercial + "', '" + streetAddress + "', '" \
                    + city + "', '" + zip + "', '" + propertyType + "', '" + ownedBy + "');"

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return "Added property"

        else:
            return "not logged in"

    @staticmethod
    def delete_property():
        if 'user' in session.keys():
            json = request.get_json()
            id = parsed_json['id']

            cursor = db.cursor()
            sql_string = "DELETE from Property WHERE id = '" + id + "'"

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return "Deleted property"
        else:
            return "not logged in"

    @staticmethod
    def get_user_properties():
        if 'user' in session.keys():
            user = session['user']
            email = user['email']
            parsed_json = request.get_json()
            sort_by = parsed_json['sort_by']
            order = parsed_json['order']

            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = "SELECT propertyName, id from Property where ownedBy = '" \
                    + email + "' ORDER BY " + sort_by + " " + order

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
    def get_other_user_properties():
        if 'user' in session.keys():
            user = session['user']
            email = user['email']
            parsed_json = request.get_json()
            sort_by = parsed_json['sort_by']
            order = parsed_json['order']

            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = "SELECT propertyName, id from Property where ownedBy != '" \
                    + email + "' ORDER BY " + sort_by + " " + order

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
    def update_property():
        if 'user' in session.keys():
            user = session['user']
            parsed_json = request.get_json()
            attribute = parsed_json['attribute']
            value = parsed_json['value']

            cursor = db.cursor()
            sql_string = ""

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            return "Update successful"
        else:
            return "not logged in"

    @staticmethod
    def get_properties_from_attribute():
        if 'user' in session.keys():
            parsed_json = request.get_json()
            attribute = parsed_json['attribute']
            value = parsed_json['value']
            sort_by = parsed_json['sort_by']
            order = parsed_json['order']

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


app.add_url_rule('/add_property', 'add_property', Property.add_property, methods=['POST'])
app.add_url_rule('/delete_property', 'delete_property', Property.delete_property, methods=['POST'])
app.add_url_rule('/get_user_properties', 'get_user_properties', Property.get_user_properties, methods=['POST'])
app.add_url_rule('/get_other_user_properties', 'get_other_user_properties', Property.get_other_user_properties, methods=['POST'])
app.add_url_rule('/update_property', 'update_property', Property.update_property, methods=['POST'])
app.add_url_rule('/get_properties_from_attribute', 'get_properties_from_attribute', Property.get_properties_from_attribute, methods=['POST'])

