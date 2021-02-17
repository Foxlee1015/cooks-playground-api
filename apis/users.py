from flask_restplus import Namespace, Resource, fields

api = Namespace('users', description='Users related operations')

users= [
    {
        "id": 1,
        "name": 'aaa'
    },
    {
        "id": 2,
        "name": 'bbb'
    }
]

@api.route('/')
class Users(Resource):
    @api.doc('list_users')
    def get(self):
        '''List all users'''
        return users

@api.route('/<id>')
@api.param('id', 'The user identifier')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get_user')
    def get(self, id):
        '''Fetch a user given its identifier'''
        for user in users:
            if user['id'] == id:
                return user
        api.abort(404)