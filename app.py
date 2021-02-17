from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/')
class Home(Resource):
    def get(self):
        return {'hello': 'home'}


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
