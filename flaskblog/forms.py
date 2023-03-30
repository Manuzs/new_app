from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 6, max = 12)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Passsword', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('SIgn Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if True:
            # return "in validate email"
            raise ValidationError('Username is already taken.')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if True:
            # return "in validate email"
            raise ValidationError('Email is already taken.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember me') 
    submit = SubmitField('Login')