from flask_restx import Api, resource, fields

from .user_models import api as people_namespace
from .file_models import api as random_namespace

api = Api(
    version='v1',
    title='Mock Data API',
    description='A simple API for getting different kinds of mock data for testing or demo purposes',
)

api.add_namespace(people_namespace)
api.add_namespace(random_namespace)

