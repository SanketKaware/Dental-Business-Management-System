from flask import render_template, session, request, redirect, url_for, flash

from dental import app, db, bcrypt

@app.route('/lab')
def lab():
    return render_template('lab.html')