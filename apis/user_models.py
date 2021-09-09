from flask_restx import Namespace, fields

api = Namespace(
    'User',
    path='/',
    description='Data for a user'
)

user_obj = {
    "name": fields.String(
        description="example of a person's name",
        example='Mike Jones'
        ),
    "address": fields.String(
        description="example of a home address",
        example='75639 Kathryn Valleys Apt. 129 Brooksshire, MD 00693'
        ),
    "phone": fields.String(
        description="example of a phone number",
        example='800.123.4567x098'
        )}


user_response = api.model(
    'User-Response', {
        **user_obj
    }
)

users_response = api.model(
    'Users-Response', {
        "user": fields.List(fields.Nested(model=user_response))
    }
)
