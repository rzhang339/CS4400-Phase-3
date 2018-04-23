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
            console.log(sql_string);
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
            sql_string = "SELECT propertyName, streetAddress, city, zip, size, propertyType, isPublic, CASE WHEN approvedBy IS NULL THEN 'False' ELSE 'True' END AS isApproved, isCommercial, Property.id, IFNULL(numVisits, 0) AS visits, ratings" \
                    + " FROM Property LEFT JOIN " \
                    + "(SELECT id, COUNT(*) AS numVisits, AVG(rating) AS ratings " \
                    + "FROM Visits Group By id) as temp ON Property.id = temp.id " \
                    + "WHERE ownedBy = '" + email + "' "\
                    + "ORDER BY " + sort_by + " " + order
            print (sql_string)
            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            properties = cursor.fetchall()
            dict_json = []
            for property in properties:
                print (property)
                property_dict = {
                    "propertyName": property['propertyName'],
                    "id": property['id'],
                    "isPublic": property['isPublic'].decode(),
                    "size": property['size'],
                    "isCommercial": property['isCommercial'].decode(),
                    "streetAddress": property['streetAddress'],
                    "city": property['city'],
                    "zip": property['zip'],
                    "propertyType": property['propertyType'],
                    "isApproved": property['isApproved'],
                    "visits": property['visits'],
                    "ratings": str(property['ratings'])
                }
                dict_json.append(property_dict)
            return_string = json.dumps(dict_json, sort_keys=True, indent=4, separators=(',', ': '))
            return return_string
        else:
            return "not logged in"

    def get_property_by_id():
        parsed_json = request.get_json()
        id = parsed_json['id']

        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql_string = "SELECT * from Property where id = '" + id + "'"

        try:
            cursor.execute(sql_string)
        except (pymysql.Error, pymysql.Warning) as e:
            print (e)
            return

        property = cursor.fetchone()
        return_string = str(property)
        return return_string


    @staticmethod
    def get_other_user_properties():
        if 'user' in session.keys():
            user = session['user']
            email = user['email']
            parsed_json = request.get_json()
            sort_by = parsed_json['sort_by']
            order = parsed_json['order']

            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = "SELECT propertyName, streetAddress, city, zip, size, propertyType, isPublic, CASE WHEN approvedBy IS NULL THEN 'False' ELSE 'True' END AS isApproved, isCommercial, Property.id, IFNULL(numVisits, 0) AS visits, ratings" \
                    + " FROM Property LEFT JOIN " \
                    + "(SELECT id, COUNT(*) AS numVisits, AVG(rating) AS ratings " \
                    + "FROM Visits Group By id) as temp ON Property.id = temp.id " \
                    + "WHERE ownedBy != '" + email + "' "\
                    + "ORDER BY " + sort_by + " " + order

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return
            properties = cursor.fetchall()
            dict_json = []
            for property in properties:
                property_dict = {
                   "propertyName": property['propertyName'],
                    "id": property['id'],
                    "isPublic": property['isPublic'].decode(),
                    "size": property['size'],
                    "isCommercial": property['isCommercial'].decode(),
                    "streetAddress": property['streetAddress'],
                    "city": property['city'],
                    "zip": property['zip'],
                    "propertyType": property['propertyType'],
                    "isApproved": property['isApproved'],
                    "visits": property['visits'],
                    "ratings": str(property['ratings'])
                }
                dict_json.append(property_dict)
            return_string = json.dumps(dict_json, sort_keys=True, indent=4, separators=(',', ': '))
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
            id = parsed_json['id']

            cursor = db.cursor()
            sql_string = "UPDATE Property SET " + attribute + " = '" + value + "' WHERE id = '" + id + "';"
            print (sql_string)
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
            sql_string = "SELECT * from Property WHERE " + attribute + " = '" + value + "' ORDER BY " + sort_by + " " + order

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            list = cursor.fetchall()
            print(list)
            for dict in list:
                dict['isPublic'] = str(dict['isPublic'])
                dict['isCommercial'] = str(dict["isCommercial"])
            return_string = json.dumps(list, sort_keys=True, indent=4, separators=(',', ': '))
            return return_string
        else:
            return "not logged in"

    @staticmethod
    def get_detailed_property():
        if 'user' in session.keys():

            parsed_json = request.get_json()
            id = parsed_json['id']
            email = parsed_json['email']


            dict = {}
            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = "SELECT propertyName, streetAddress, city, zip, size, propertyType, isPublic, CASE WHEN approvedBy IS NULL THEN 'False' ELSE 'True' END AS isApproved, isCommercial, Property.id, IFNULL(numVisits, 0) AS visits, ratings" \
                        + " FROM Property LEFT JOIN " \
                        + "(SELECT id, COUNT(*) AS numVisits, AVG(rating) AS ratings " \
                        + "FROM Visits Group By id) as temp ON Property.id = temp.id " \
                        + "WHERE Property.id = " + id  + ";"
            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            property = cursor.fetchone()
            dict.update(property)

            sql_string = "SELECT username, email FROM User WHERE email = '" + email + "';"
            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            property = cursor.fetchone()
            dict.update(property)

            sql_string = "SELECT produceName, produceType FROM FarmGrows NATURAL JOIN Produce WHERE id = " + id + ";"
            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            produces = cursor.fetchall()
            produce_dict = {}
            for produce in produces:
                if produce['produceType'] not in produce_dict.keys():
                    produce_dict[produce['produceType']] = [produce['produceName']]
                else:
                    produce_dict[produce['produceType']].append(produce['produceName'])
            dict.update(produce_dict)

            print (dict)
            dict['isPublic'] = str(dict['isPublic'])
            dict['isCommercial'] = str(dict['isCommercial'])
            dict['ratings'] = str(dict['ratings'])
            return json.dumps(dict, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            return "not logged in"

    @staticmethod
    def get_unconfirmed_properties():
        if 'user' in session.keys():
            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql_string = "SELECT * " \
                    + "FROM Property JOIN User ON Property.ownedBy = User.email " \
                    + "WHERE approvedBy IS NULL " \
                    + "ORDER BY propertyName ASC;"

            try:
                cursor.execute(sql_string)
            except (pymysql.Error, pymysql.Warning) as e:
                print (e)
                return

            list = cursor.fetchall()
            print (list)
            for dict in list:
                print (dict)
                dict['isPublic'] = str(dict['isPublic'])
                dict['isCommercial'] = str(dict['isCommercial'])

            return json.dumps(list, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            return "not logged in"



app.add_url_rule('/add_property', 'add_property', Property.add_property, methods=['POST'])
app.add_url_rule('/delete_property', 'delete_property', Property.delete_property, methods=['POST'])
app.add_url_rule('/get_user_properties', 'get_user_properties', Property.get_user_properties, methods=['POST'])
app.add_url_rule('/get_other_user_properties', 'get_other_user_properties', Property.get_other_user_properties, methods=['POST'])
app.add_url_rule('/update_property', 'update_property', Property.update_property, methods=['POST'])
app.add_url_rule('/get_properties_from_attribute', 'get_properties_from_attribute', Property.get_properties_from_attribute, methods=['POST'])
app.add_url_rule('/get_property_by_id', 'get_property_by_id', Property.get_property_by_id, methods=['POST'])
app.add_url_rule('/get_detailed_property', 'get_detailed_property', Property.get_detailed_property, methods=['POST'])
app.add_url_rule('/get_unconfirmed_properties', 'get_unconfirmed_properties', Property.get_unconfirmed_properties, methods=['GET'])




