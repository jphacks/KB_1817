from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from jinja2 import FileSystemLoader

app = Flask(__name__)
app.jinja_loader = FileSystemLoader('./templates')
app.config.from_object('charin.config')

db = SQLAlchemy(app)

import charin.views