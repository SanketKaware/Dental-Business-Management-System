from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dentaldb.db'
app.config['SECRET_KEY']='some_secrete'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from dental.user import routes
from dental.products import routes
from dental.carts import carts