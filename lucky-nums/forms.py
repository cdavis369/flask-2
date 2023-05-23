from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange, Email

class LuckyNumberForm(FlaskForm):
  """Form for user to get their lucky"""
  name = StringField("Name", validators=[DataRequired()])
  birthyear = IntegerField("Birth year", validators=[DataRequired(), NumberRange(min=1900, max=2000, message="Must from 1900 through 2000")])
  email = StringField("Email", validators=[DataRequired(), Email()])
  colors = SelectField("Color", coerce=int)