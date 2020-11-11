from . import app
from flask import render_template, request, redirect, session, url_for, abort
"""
import os
os.urandom(24)
"""
app.secret_key = '123456789'

@app.route('/')
def index():
    title = 'Index'
    return render_template('base.html.j2', title=title)

@app.route('/info/')
def info():
    title = 'Info'
    return render_template('info.html.j2', title=title)

@app.route('/info/',methods=['GET','POST'])
def info_post():
    jmeno = request.form.get('jmeno')
    heslo = request.form.get('heslo')
    if heslo == 'heslo':
        session['user'] = jmeno
    print(jmeno,heslo)
    return redirect(url_for('index'))

@app.route('/logout/',methods=['GET','POST'])
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/tajné/',methods=['GET'])
def tajné():
    if 'user' in session:
        return render_template('tajné.html.j2')
    else:
        return abort(403)

@app.route('/obdelník/')
def obdelník():
    title = 'Obdelník'
    x = request.args.get('x')
    y = request.args.get('y')
    try:
        z = int(x) * int(y)
        n = 2 * (int(x) + int(y))
    except (TypeError, ValueError):
        z = ''
        n = ''
    return render_template('obdelník.html.j2', title=title, z=z, n=n)

@app.route('/čtverec/')
def čtverec():
    title = 'Čtverec'
    x = request.args.get('x')
    try:
        z = int(x) * int(x)
        n = 4 * int(x)
    except (TypeError, ValueError):
        z = ''
        n = ''
    return render_template('čtverec.html.j2', title=title, z=z, n=n)


