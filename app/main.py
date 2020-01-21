#!/usr/bin/env python3

#https://www.flaskapi.org/

import requests
#TODO promazat import
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

def getTotalUsers(html):
    start = html.find('<div class="pagination">')
    users = html[start:start+100].split()[2]
    return int(users)

def countMembersHtml(html):
    pageUsers = html.count('./memberlist.php?mode=viewprofile&amp;')
    unregistred = html.count('Uživatel fóra – není člen Pirátů')
    registred = html.count('Příznivec Pirátů –')
    return pageUsers - unregistred - registred

def countMembers():
    r = requests.get('https://forum.pirati.cz/memberlist.php')
    total = getTotalUsers(r.text)
    users = countMembersHtml(r.text)
    for i in range(100,total,100):
        r = requests.get('https://forum.pirati.cz/memberlist.php?start='+str(i))
        users += countMembersHtml(r.text)
    return users


@app.route('/members/')
def example():
    return {'members': countMembers()}


if __name__ == "__main__":
    app.run(debug=True)
