
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
# inheritance
# BasicForm inherits from FlaskForm
# BasicForm is now a kind of FlaskForm
class BasicForm(FlaskForm):
    # instantiating various input fields
    firstname = StringField('First Name:')
    surname = StringField('Last Name:')
    age = StringField('Age:')
    email = StringField('Email:')
    iracing_id = StringField("iRacing Subscriber: Y or N?")
    submit = SubmitField('Register')