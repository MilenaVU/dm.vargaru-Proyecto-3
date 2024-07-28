import os
#conexionn a la base de datos Mysql
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key' 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:Ch*col4t3.@localhost/heladeria_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
