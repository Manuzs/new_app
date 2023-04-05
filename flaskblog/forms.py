from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 6, max = 12)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Passsword', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            # return "in validate email"
            raise ValidationError('Username is already taken.')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            # return "in validate email"
            raise ValidationError('Email is already taken.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember me') 
    submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                             validators = [DataRequired(), Length(min = 6, max = 12)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpeg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username :
            user = User.query.filter_by(username=username.data).first()
            if user:
            # return "in validate email"
                raise ValidationError('Username is already taken.')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            # return "in validate email"
            if user:
                raise ValidationError('Email is already taken.')