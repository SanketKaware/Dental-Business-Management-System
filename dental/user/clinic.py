from flask import render_template, session, request, redirect, url_for, flash

from dental import app, db, bcrypt

@app.route('/clinic')
def clinic():
    return render_template('clinic.html')