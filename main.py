from flask import Flask
from flask_restx import Resource
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from handlers.places import place, places
from handlers.people import person, people
from apis import api
from apis.user_models import person_response, people_response
from apis.file_models import place_response, places_response
from apis.ex_models import thing_response, things_response

app = Flask(__name__)
api.init_app(app)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    application_limits=["100 per hour", "15 per minute", "9 per second"],
    default_limits=["100 per hour", "15 per minute", "9 per second"]
)


peopleEndpoints = api.namespace(
    'People',
    path='/',
    description='Endpoints that output human-like data'
)

placesEndpoints = api.namespace(
    'Places',
    path='/',
    description='Endpoints that output place data'
)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return 'Hello, World!'


@peopleEndpoints.route('/person', methods=['GET'])
class Person(Resource):
    @peopleEndpoints.response(code=200, model=person_response, description='')
    def get(self):
        '''returns example data representative of a person'''
        return person()


@peopleEndpoints.route('/people', methods=['GET'])
class People(Resource):
    @peopleEndpoints.response(code=200, model=people_response, description='')
    def get(self):
        '''returns example data representative of several people'''
        return people()


@placesEndpoints.route('/place', methods=['GET'])
class Place(Resource):
    @peopleEndpoints.response(code=200, model=place_response, description='')
    def get(self):
        '''returns example data representative of a place'''
        return place()


@placesEndpoints.route('/places', methods=['GET'])
class Places(Resource):
    @peopleEndpoints.response(code=200, model=places_response, description='')
    def get(self):
        '''returns example data representative of several places'''
        return places()


@placesEndpoints.route('/places', methods=['POST'])
class Things(Resource):
    @peopleEndpoints.response(code=200, model=things_response, description='')
    def post(self):
        '''returns example data representative of several places'''
        return things()


if __name__ == '__main__':
    app.run(debug=True)
