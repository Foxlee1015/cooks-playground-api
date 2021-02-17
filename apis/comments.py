from flask_restplus import Namespace, Resource, fields

api = Namespace('comments', description='Comments related operations')

comments = [
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
class Comments(Resource):
    @api.doc('list_comments')
    def get(self):
        '''List all comments'''
        return comments

@api.route('/<id>')
@api.param('id', 'The comment identifier')
@api.response(404, 'Comment not found')
class Comment(Resource):
    @api.doc('get_comments')
    def get(self, id):
        '''Fetch a comment given its identifier'''
        for comment in comments:
            if comment['id'] == id:
                return comment
        api.abort(404)