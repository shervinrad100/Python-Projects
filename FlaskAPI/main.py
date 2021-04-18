from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_intro import db, Table
from flask_marshmallow import Marshmallow

# initialise Flask app and initialise API as a Flask app
app = Flask(__name__)
api = Api(app)

# create sqlite db in dir (relative path), create a db obj for your app 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)

# init marshmallow to convert table return object to serializable format
ma = Marshmallow(app)
class TableSchema(ma.Schema):
    class Meta:
        fileds = ('id', 'othercol', 'date_created')




# # create your db model and initialise db
# class Table(db.Model):
#     # __tablename__ = 'Table'
#     id = db.Column(db.Integer, primary_key=True)
#     othercol = db.Column(db.String(100))
#     date_created = db.Column(db.DateTime, default=datetime.now)

#     def __repr__(self):
#         '''if you print the obj you want it to return to stdout not the obj return type'''
#         return f"Table(col={id})"

# db.create_all()



# create a requests parser that parses the query
endpnt_method_args = reqparse.RequestParser()
endpnt_method_args.add_argument("id", type=str, help="id description [required= True|False]", required=True)
endpnt_method_args.add_argument("othercol", type=str, help="othercol description [required= True|False]")


# you need to serialize your db return obj so you can return them over http
resource_fileds = {
    'id': fields.Integer,
    'othercol': fields.String
}


# define methods for a specific class of resources
class Home(Resource):
    
    # abort craetes a catch for bad queries
    @staticmethod
    def abort_if_request_doest_exist(id_):
        result = Table.query.filter_by(id=id_).all()
        if not result:
            abort(404, "error message")
        else:
            return result
            
    @marshal_with(resource_fileds)
    def get(self, id_):
        '''what the decorator does is that it takes the return value and serializes with the resource_fileds items'''
        result = abort_if_request_doest_exist(id_)
        table_schema = TableSchema(many=True, strict=True)
        output = table_schema.dump(result)#.data
        return jsonify({"page":"home", "data":output})

    @marshal_with(resource_fileds)
    def put(self, id_, other=None):
        '''you submit an id, i look in db and try to match the predefined args to query your request
        returns serialised db object and status code
        if arg is required and key:val for it not provided you get an error'''
        args = endpnt_method_args.parse_args()
        row = Table(id=id_, other=args['othercol'])
        db.session.add(row)
        db.session.commit()
        return row, 201


# declare a resource and assign an endpoint to it, if parameters are passed, define them in "<dType: paramName>"
api.add_resource(Home, "/home")


# run web app microservice if script is run (in debug mode)
if __name__ == '__main__':
    app.run(debug=True)
