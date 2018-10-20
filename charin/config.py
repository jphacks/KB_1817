import os

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{dbname}?charset=utf8'.format(**{
        'user': os.getenv('DB_USERNAME'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'dbname': os.getenv('DB_DATABASE')
    })
SECRET_KEY = 'secret key'
SQLALCHEMY_TRACK_MODIFICATIONS = True