import os


class Config:
    SECRET_KEY = '5ef9e49a4ece37050f2aefeea1a965c3'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///..//instance/site.db' 
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'user@gmail.com'# your mail here
    MAIL_PASSWORD = '************' #your mail app password here
