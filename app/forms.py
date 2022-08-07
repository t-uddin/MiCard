from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

from helpers.auth_validators import safe_string, unique_or_current_user_field


class editProfileForm(FlaskForm):
    forename = StringField("Forename", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    voice = SelectField("Voice", choices=[("male", "Male"), ("female", "Female")], validators=[DataRequired()])
    submit = SubmitField("Confirm Changes")


class RegistrationForm(FlaskForm):
    """Register a new user with email, username, and password"""
    email = StringField(
        "Email",
        description="Email",
        validators=[
            DataRequired(),
            Email(),
            unique_or_current_user_field("Email is already registered."),
        ],
    )
    forename = StringField(
        "First Name",
        description="Forename",
        validators=[DataRequired(), Length(min=1, max=80)],
    )
    surname = StringField(
        "Surname",
        description="Surname",
        validators=[DataRequired(), Length(min=1, max=80)],
    )
    password = PasswordField(
        "Password",
        description="Password",
        validators=[DataRequired(), Length(min=5, max=40)],
    )
    confirm_psw = PasswordField(
        "Confirm password",
        description="Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("pass_confirm", message="Passwords Must Match!"),
        ],
    )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    """Allow users to log in with username or email compared against a pw"""

    username_or_email = StringField(
        "Username or email",
        description="Username or email",
        validators=[DataRequired()],
    )
    password = PasswordField(
        "Password", description="Password", validators=[DataRequired()]
    )
    submit = SubmitField("Log In")


class SettingsForm(FlaskForm):
    """Allow users to update their name, username, email, and password"""

    name = StringField(
        "Name", description="John Smith", validators=[Optional(), Length(max=80)],
    )
    username = StringField(
        "Username",
        description="Username",
        validators=[
            DataRequired(),
            unique_or_current_user_field("Username already exists."),
            safe_string(),
            Length(min=3, max=40),
        ],
    )
    email = StringField(
        "Email",
        description="my@email.com",
        validators=[
            DataRequired(),
            Email(),
            unique_or_current_user_field("Email is already registered."),
        ],
    )
    new_pass = PasswordField(
        "New Password",
        description="New password",
        validators=[Optional(), Length(min=8, max=30)],
    )
    pass_confirm = PasswordField(
        "Confirm password",
        description="Confirm password",
        validators=[Optional(), EqualTo("new_pass", message="Passwords Must Match!")],
    )
    submit = SubmitField("Update")