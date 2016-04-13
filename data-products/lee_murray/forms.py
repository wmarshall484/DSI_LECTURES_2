from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class DataForm(Form):
    user_name = StringField('What is your name?', validators=[DataRequired()])
    favorite_color = StringField('What is your favorite color', validators=[DataRequired()])
    real_person = BooleanField('Are you real?')