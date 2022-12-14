from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, PasswordField, IntegerField, FieldList, DecimalField, TelField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
from wtforms import validators
from helpers.auth_validators import unique_or_current_user_field


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
            EqualTo("confirm_psw", message="Passwords Must Match!"),
        ],
    )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    """Allow users to log in with username or email compared against a pw"""

    email = StringField(
        "Email",
        description="Enter email",
        validators=[DataRequired()],
    )
    password = PasswordField(
        "Password", description="Enter Password", validators=[DataRequired()]
    )
    submit = SubmitField("Login")


class CreateProfileForm(FlaskForm):
    """Create a newly registered users profile"""
    bio = TextAreaField(
        "Bio",
        description="Add a bit about yourself..",
        validators=[
            DataRequired(),
        ],
    )
    email = StringField(
        "Contact Email",
        description="example@email.com",
        validators=[
            DataRequired(),
            Email(),
        ],
    )
    job = StringField(
        "Job Title",
        description="Add job title",
        validators=[DataRequired()]
    )
    field = StringField(
        "Field",
        description="Add field",
        validators=[DataRequired()]
    )
    phone = TelField(
        "Contact Number",
        description="Add contact number",
        validators=[
            DataRequired()
        ],
    )
    hours = StringField(
        "Working Hours",
        description="Add working hours",
        validators=[DataRequired()]
    )
    location = StringField(
        "Location",
        description="Add work location",
        validators=[DataRequired()]
    )
    registration = StringField(
        "Registration",
        description="Add registration",
        validators=[DataRequired()]
    )
    years = IntegerField(
        "Years of Experience",
        description="0",
        validators=[DataRequired()]
    )
    fee = DecimalField(
        "Consultation Fee",
        description=0.00,
        validators=[DataRequired()]
    )
    # specialisms = FieldList(StringField(
    #                         "Specialisms",
    #                         description="Add a specialism",
    #                         validators=[DataRequired()]), min_entries=1)

    specialisms = StringField(
        "Specialisms",
        description="Add a specialism",
        validators=[DataRequired()]
    )

    treatments = StringField(
        "Treatments",
        description="Add a treatment",
        validators=[DataRequired()]
    )

    certifications = StringField(
        "Certifications",
        description="Add a certification",
        validators=[DataRequired()]
    )

    education = StringField(
        "Education",
        description="Add a specialism",
        validators=[DataRequired()]
    )

    interests = StringField(
        "Interests",
        description="Add an interest",
        validators=[DataRequired()]
    )

    submit = SubmitField("Save")
