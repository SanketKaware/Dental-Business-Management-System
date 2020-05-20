from flask import render_template, session, request, redirect, url_for, flash, session

from dental import app, db, bcrypt
from dental.products.models import lab_product, manufacturer_product

@app.route('/lab')
def lab():
    if 'username' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login', filename='routes.py'))
    products=lab_product.query.all()
    return render_template('lab.html', title= 'Lab User', products=products)

