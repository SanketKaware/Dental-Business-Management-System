from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import IntegerField, StringField, BooleanField, TextAreaField, validators, Form, DecimalField

class manufacturer_products(Form):
    name = StringField('Name', [validators.DataRequired()])
    seller = StringField('Seller', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    description = TextAreaField('description', [validators.DataRequired()])

class lab_products(Form):
    name = StringField('Name', [validators.DataRequired()])
    seller = StringField('Seller', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])