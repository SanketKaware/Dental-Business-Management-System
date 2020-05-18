from flask import render_template, session, request, redirect, url_for, flash
from dental import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User
from .lab import lab
from .clinic import clinic
from .manufacturer import manufacturer

# @app.route('/user')
# def user():
#     if 'username' not in session:
#         flash(f'Please login first','danger')
#         return redirect(url_for('login'))
#     # products = Addproduct.query.all()
#     return render_template('user/index.html', title='User Page')

@app.route('/')
def homepage():
    return redirect(url_for("login"))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data,
                    password=hash_password, role_id=form.role_id.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.username.data}. Thank you for registering','success')
        return redirect(url_for('login'))
    return render_template('user/register.html', form=form, title="Registration page")

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(username = form.username.data, role_id = '2').first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['username']= form.username.data
            flash(f'Welcome {form.username .data}. You are logged in successfully.', 'success')
            return redirect(request.args.get('next') or url_for('lab'))
        else:
            flash('Wrong credentials. Please try again', 'danger')

    if request.method == "POST" and form.validate():
        user = User.query.filter_by(username = form.username.data, role_id = '1').first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['username']= form.username.data
            flash(f'Welcome {form.username .data}. You are logged in successfully.', 'success')
            return redirect(request.args.get('next') or url_for('clinic'))
        else:
            flash('Wrong credentials. Please try again', 'danger')

    if request.method == "POST" and form.validate():
        user = User.query.filter_by(username = form.username.data, role_id = '3').first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['username']= form.username.data
            flash(f'Welcome {form.username .data}. You are logged in successfully.', 'success')
            return redirect(request.args.get('next') or url_for('manufacturer'))
        else:
            flash('Wrong credentials. Please try again', 'danger')

    return render_template('user/login.html', form=form, title='Login Page')