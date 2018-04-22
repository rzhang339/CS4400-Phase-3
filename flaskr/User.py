import pymysql
from flask import request, session, Response
import hashlib
from flaskr import app, db
import json

class User():

    @staticmethod
    def register():
        json = request.get_json()
        username = json['username']
        email = json['email']
        password = User.hash_password(json['password'])
        type = json['type']
        
        cursor = db.cursor()
        sql_string = "INSERT INTO User (email, username, password, userType) VALUES ('" \
                + email + "', '" \
                + username + "', '" \
                + password + "', '" \
                + type + "');"

        try:
            cursor.execute(sql_string)
        except (pymysql.Error, pymysql.Warning) as e:
            cursor.close()
            return "Invalid"

        cursor.close()
        return "Registered"

    @staticmethod
    def login():
        parsed_json = request.get_json()
        email = parsed_json['email']
        password = User.hash_password(parsed_json['password'])

        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql_string = "SELECT username, password, userType FROM User WHERE email = '" \
                + email + "' AND password = '" + password + "'"

        try:
            cursor.execute(sql_string)
        except (pymysql.Error, pymysql.Warning) as e:
            cursor.close()
            return "Invalid"

        user = cursor.fetchone()
        cursor.close()
        if user is not None:
            print (user)
            if 'user' in session.keys():
                return "Already Logged In"
            user['email'] = email
            session['user'] = user
            return user['userType']
        else:
            return "Invalid Login"

    @staticmethod
    def logout():
        if 'user' not in session.keys():
            return "Already Logged Out"
        else:
            session.pop('user', None)
            return "logout"


    @staticmethod
    def get_session():
        if 'user' in session.keys():
            return json.dumps(session['user'], sort_keys=True, indent=4, separators=(',', ': '))
        else:
            return "not logged in"

    def hash_password(password):
        return hashlib.md5(bytes(password.encode())).hexdigest()

app.add_url_rule('/register', 'register', User.register, methods=['POST'])
app.add_url_rule('/login', 'login', User.login, methods=['POST'])
app.add_url_rule('/logout', 'logout', User.logout, methods=['GET'])
app.add_url_rule('/get_session', 'get_session', User.get_session, methods=['GET'])

