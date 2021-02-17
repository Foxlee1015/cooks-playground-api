from flask_restplus import Namespace, Resource, fields

api = Namespace('sessions', description='Sessions related operations')

sessions = [
    {
        "id": 1,
        "name": 'water'
    },
    {
        "id": 2,
        "name": 'coke'
    }
]

@api.route('/')
class Sessions(Resource):
    @api.doc('list_sessions')
    def get(self):
        '''List all sessions'''
        return sessions

@api.route('/<id>')
@api.param('id', 'The session identifier')
@api.response(404, 'Session not found')
class Session(Resource):
    @api.doc('get_sessions')
    def get(self, id):
        '''Fetch a session given its identifier'''
        for session in sessions:
            if sessions['id'] == id:
                return sessions
        api.abort(404)