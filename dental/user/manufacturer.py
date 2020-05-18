from flask import render_template, session, request, redirect, url_for, flash

from dental import app, db, bcrypt

@app.route('/manufacturer')
def manufacturer():
    return render_template('manufacturer.html')