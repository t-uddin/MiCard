from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class editProfileForm(FlaskForm):
    forename = StringField("Forename", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    voice = SelectField("Voice", choices=[("male", "Male"), ("female", "Female")], validators=[DataRequired()])
    submit = SubmitField("Confirm Changes")