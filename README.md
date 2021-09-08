# Flask-Mock-Data-Api
Api written in Python Flask that can be used to retrieve mock data. 
It has Swagger 2.0 documentation automatically generated using the Flask-restx/flask-restplus library.
It comes with pre-configured IP address level rate limiting via Flask-Limiter and is ready to be deployed to Heroku.

## Installation
`pip install -r requirements.txt`

## Running instructions
Run `python main.py` with the requirements installed.
Navigate to `localhost://5000` or `http://127.0.0.1:5000/`
to view the swagger documentation.