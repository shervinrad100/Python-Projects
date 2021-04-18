# FlaskAPI

Following: https://www.youtube.com/watch?v=GMppyAPbLYk

Notes:
- your response formats should be JSON and XML serializable eg: string, int and other primitive dTypes
    - serialization means that you can convert object to string eg: {foo:[1,2,3], bar:"yes"} --> '{"foo":[1,2,3], "bar": "yes"}'



# TODO
- connect DB to API
    1. find out why tab_schema.dump(result) returns [{}] (test.py)
    2. create DB in (SQLAlchemy_intro.py) 
    3. query the tables from (main.py)

- learn SQLAlchemy/SQLite
