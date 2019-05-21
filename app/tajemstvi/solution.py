import functools
import flask

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from tajemstvi.db import get_db

bp = Blueprint('solution', __name__, url_prefix='/')

def check(solution):
    def clean(solution):
        tabulka = tabulka =dict(zip("áčďéěíňóřšťúůüýžabcdefghijklmnopqrstuvwxyz","acdeeinorstuuuyzabcdefghijklmnopqrstuwxyz"))
        cleaned = []
        for char in solution:
            if char in tabulka:
                cleaned.append(tabulka[char])
            else:
                cleaned.append(char)
        return "".join(cleaned)
    cleaned = clean(solution.lower())
    return cleaned == "buresicau"


@bp.route('/', methods=('GET', 'POST'))
def solve():
    if request.method == 'POST':
#        nickname = request.form['nickname']
        solution = request.form['solution1'] + request.form['solution2'] + request.form['solution3'] + request.form['solution4'] + request.form['solution5'] + request.form['solution6'] + request.form['solution7'] + request.form['solution8'] + request.form['solution9']
        db = get_db()
        error = None

        if check(solution):
            rows = db.execute(
                    'SELECT COUNT(*) FROM solution'
                    ).fetchall()
            rows = rows[0][0]
            if rows < 9000:
                cursor = db.execute(
                    'INSERT INTO solution (nickname) VALUES (?)',
                    ('nickname',)
                )
                score = cursor.lastrowid
                db.commit()
                session.clear()
                session['score'] = score
                return redirect(url_for('solution.correct'))
            else:
                return redirect(url_for('solution.correct'))
        else:
            #error = 'Dekujeme za pokus, ale  "{}" neni spravne reseni.'.format(solution)
            #flash(error)
            return redirect(url_for('solution.incorrect'))

    return render_template('solve.html')

@bp.route('/incorrect', methods=('GET',))
def incorrect():
    return render_template('incorrect.html')

@bp.route('/correct', methods=('GET',))
def correct():
    return render_template('correct.html',score=session['score'])
