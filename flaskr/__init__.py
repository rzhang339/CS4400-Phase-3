from flask import Flask
from flask import request

from flaskr import app

# db.create_all()

if __name__ == '__main__':
	app.run(host = "0.0.0.0", port = 5000)