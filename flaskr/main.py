from flask import Flask
from flask import request

import User
import Property
import Produce
import Visits

from flaskr import app


def apply_caching(response):
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

if __name__ == '__main__':
	app.run()