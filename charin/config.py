import os

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/charin?charset=utf8'.format(**{
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'host': os.getenv('DB_HOST', 'localhost'),
    })
SECRET_KEY = 'secret key'
SQLALCHEMY_TRACK_MODIFICATIONS = True