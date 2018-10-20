from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config.from_object('charin.config')

db = SQLAlchemy(app)

import charin.views