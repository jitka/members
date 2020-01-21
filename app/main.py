#!/usr/bin/env python3

#https://www.flaskapi.org/

import requests
from members import create_app #TODO promazat import
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)


def countMembersHtml(html):
    pageUsers = html.count('./memberlist.php?mode=viewprofile&amp;')
    unregistred = html.count('Uživatel fóra – není člen Pirátů')
    registred = html.count('Příznivec Pirátů –')
    return pageUsers - unregistred - registred

def countMembers(total):
    #TODO prvni a posledni
    for i in range(100,total,100):
        r = requests.get('https://forum.pirati.cz/memberlist.php?start='+str(i))
        print(countMembersHtml(r.text))

@app.route('/members/')
def example():
    return {'members': 11488}

if __name__ == "__main__":
    print(countMembers(11519))
    #app.run(debug=True)
