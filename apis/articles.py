from flask_restplus import Namespace, Resource, fields

api = Namespace('articles', description='Articles related operations')

articles = [
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
class Articles(Resource):
    @api.doc('list_articles')
    def get(self):
        '''List all articles'''
        return articles

@api.route('/<id>')
@api.param('id', 'The article identifier')
@api.response(404, 'Article not found')
class Article(Resource):
    @api.doc('get_articles')
    def get(self, id):
        '''Fetch an article given its identifier'''
        for articles in articles:
            if article['id'] == id:
                return article
        api.abort(404)