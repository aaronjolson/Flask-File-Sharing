import logging

from flask import Flask, g, request, jsonify
from flask_restx import Resource
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sqlite3 as sql

from handlers.files import file, files
from handlers.users import user, users
from apis import api
from apis.user_models import user_response, users_response
from apis.file_models import file_response, files_response

app = Flask(__name__)
api.init_app(app)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    application_limits=["100 per hour", "15 per minute", "9 per second"],
    default_limits=["100 per hour", "15 per minute", "9 per second"]
)


userEndpoints = api.namespace(
    'Users',
    path='/',
    description='Endpoints that output user data'
)

fileEndpoints = api.namespace(
    'Files',
    path='/',
    description='Endpoints that output place data'
)


DATABASE = '/path/to/database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return 'Hello, World!'


@userEndpoints.route('/user', methods=['GET'])
class User(Resource):
    @userEndpoints.response(code=200, model=user_response, description='')
    def get(self):
        '''returns example data representative of a user'''
        return user()


@userEndpoints.route('/users', methods=['GET'])
class People(Resource):
    @userEndpoints.response(code=200, model=users_response, description='')
    def get(self):
        '''returns example data representative of several users'''
        return users()


@fileEndpoints.route('/file', methods=['GET'])
class File(Resource):
    @fileEndpoints.response(code=200, model=file_response, description='')
    def get(self):
        '''returns example data representative of a place'''
        return file()


@fileEndpoints.route('/files', methods=['GET'])
class Files(Resource):
    @fileEndpoints.response(code=200, model=files_response, description='')
    def get(self):
        '''returns example data representative of several files'''
        return files()


def setup():
    conn = sql.connect('database.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS records (name TEXT, address TEXT, city TEXT)')
    print("Table created successfully")
    conn.close()


setup()


@app.route('/records', methods=['POST', 'GET'])
def record():
    if request.method == 'POST':
        msg = ''
        try:
            data = request.json
            name = data['name']
            address = data['address']
            city = data['city']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO records (name, address, city) VALUES(?, ?, ?)", (name, address, city))
                con.commit()
                msg = "Record successfully added"
        except Exception as e:
            con.rollback()
            logging.exception(e)

        finally:
            return jsonify(msg)

    if request.method == 'GET':
        con = sql.connect("database.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("select * from records")
        columns = [column[0] for column in cur.description]

        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append(dict(zip(columns, row)))

        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
