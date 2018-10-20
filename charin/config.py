import os

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{dbname}?charset=utf8'.format(**{
        'user': os.getenv('DB_USERNAME',"root"),
        'password': os.getenv('DB_PASSWORD',""),
        'host': os.getenv('DB_HOST','localhost'),
        'dbname': os.getenv('DB_DATABASE','charin')
    })
SECRET_KEY = 'secret key'
SQLALCHEMY_TRACK_MODIFICATIONS = True