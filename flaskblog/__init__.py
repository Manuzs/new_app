from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 


app = Flask(__name__)
app.config['SECRET_KEY'] = '5ef9e49a4ece37050f2aefeea1a965c3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
db = SQLAlchemy(app)
bcrpyt = Bcrypt(app)
login_manager = LoginManager(app)


from flaskblog import routes

