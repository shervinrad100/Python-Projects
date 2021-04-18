from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime


# initialise flask app
app = Flask(__name__)


# create database in config route 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# create your db model and initialise db
class Table(db.Model):
    # __tablename__ = 'Table'
    id = db.Column(db.Integer, primary_key=True)
    othercol = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        '''if you print the obj you want it to return to stdout not the obj return type'''
        return f"Table(col={id})"

db.create_all()

