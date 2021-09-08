from flask_restx import Namespace, fields

api = Namespace(
    'File Data',
    path='/',
    description='Some thing data'
)

thing_obj = {
    "**any_json**": fields.String(
        description="anything you want",
        example='turtle <( )>'
        )
}


thing_response = api.model(
    'Thing-Response', {
        **thing_obj
    }
)

things_response = api.model(
    'Things-Response', {
        "things": fields.List(fields.Nested(model=thing_response))
    }
)
