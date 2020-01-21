#!/usr/bin/env python3

#https://www.flaskapi.org/

from members import create_app #TODO promazat import
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route('/members/')
def example():
    return {'members': 11488}

if __name__ == "__main__":
    app.run(debug=True)
