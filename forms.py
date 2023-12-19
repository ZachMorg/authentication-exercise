from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(message="Username can't be left blank"), Length(max=20, message="Username must be no longer than 20 characters long")])
    password = PasswordField('Password', validators=[InputRequired(message="Password can't be left blank")])
    email = StringField('Email', validators=[InputRequired(message="Email can't be left blank"), Email(), Length(max=50, message="Email must be no longer than 50 characters")])
    first_name = StringField('First Name', validators=[InputRequired(message="First name can't be left blank"), Length(max=30, message="First name must be no longer than 30 characters")])
    last_name = StringField('Last Name', validators=[InputRequired(message="Last name can't be left blank"), Length(max=30, message="Last name must be no longer than 30 characters")])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(message="Username can't be left blank"), Length(max=20, message="Username must be no longer than 20 characters long")])
    password = PasswordField('Password', validators=[InputRequired(message="Password can't be left blank")])

class FeedbackForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(message="Title can't be left blank"), Length(max=100, message="Title must be no longer than 100 characters long")])
    content = StringField('Content', validators=[InputRequired(message="Content can't be left blank")])