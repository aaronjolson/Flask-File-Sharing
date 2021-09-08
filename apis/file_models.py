from flask_restx import Namespace, fields

api = Namespace(
    'File Data',
    path='/',
    description='file data'
)

file_obj = {
    "name": fields.String(
        description="example of a person's name",
        example='38.70734'
        ),
    "type": fields.String(
        description="example of a home address",
        example='-77.02303'
        ),
    "size": fields.String(
        description="example of a phone number",
        example='Fort Washington'
        ),
    "": fields.String(
        description="country code",
        example='US'
        ),
    "": fields.String(
        description="timezone",
        example='America/New_York'
        )
}


place_response = api.model(
    'File-Response', {
        **file_obj
    }
)

places_response = api.model(
    'Places-Response', {
        "places": fields.List(fields.Nested(model=place_response))
    }
)
