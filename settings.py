import os
FLASK_APP = 'run'
SERVER_HOST_NAME = "localhost"
SQLALCHEMY_DATABASE_URI = os.path.join('postgres://krbasfbcuwugru:ecd961db27e0cfe5411b8fb0ee92ac03a68dc232d8ebdcd98879c4661fe82787@ec2-54-165-164-38.compute-1.amazonaws.com:5432/df5rtq003qd3el')
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS',True)

MYSQL_DATABASE_USER = "dev"
MYSQL_DATABASE_PASSWORD = "dev"
MYSQL_DATABASE_DB = "basket"
MYSQL_DATABASE_HOST = "localhost"
MYSQL_DATABASE_PORT = "3306"
SERVER_HOST_NAME = "app_user.mysql"

#SQLALCHEMY_DATABASE_URI = os.path.join('mysql+pymysql://dev:dev@localhost:3306/basket')
#SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS',True)


HOST = '0.0.0.0'
PORT = str(os.environ.get("PORT", 5000))
DEBUG = True
SECRET_KEY = 'basket'