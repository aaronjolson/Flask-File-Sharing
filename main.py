from flask import Flask
from flask_restx import Resource
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from handlers.files import file, files
from handlers.user import user, users
from apis import api
from apis.user_models import user_response, users_response
from apis.file_models import file_response, files_response
from apis.ex_models import thing_response, things_response

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


if __name__ == '__main__':
    app.run(debug=True)
