import os
FLASK_APP = 'run'
MYSQL_DATABASE_USER = "dev"
MYSQL_DATABASE_PASSWORD = "dev"
MYSQL_DATABASE_DB = "basket"
MYSQL_DATABASE_HOST = "localhost"
MYSQL_DATABASE_PORT = "3306"
SERVER_HOST_NAME = "localhost"
SQLALCHEMY_DATABASE_URI = os.path.join('mysql+pymysql://dev:dev@localhost/basket')
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS',True)

HOST = 'localhost'
PORT = '5002'
DEBUG = True
SECRET_KEY = 'basket'