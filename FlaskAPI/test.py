from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_intro import db, Table
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)

ma = Marshmallow(app)
class TableSchema(ma.Schema):
    class Meta:
        fileds = ('id', 'othercol', 'date_created')


tab_schema = TableSchema(many=True)
result = Table.query.all()
output = tab_schema.dump(result)
print(result[0].othercol, output)