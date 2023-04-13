import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = '5ef9e49a4ece37050f2aefeea1a965c3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///..//instance/site.db' 
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ranjitdav350@gmail.com'
app.config['MAIL_PASSWORD'] = 'lwqq ovhd vfzp uhgu'
mail = Mail(app)

from flaskblog import routes

