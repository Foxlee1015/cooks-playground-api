from flask_restplus import Namespace, Resource, fields

api = Namespace('ingredients', description='Ingredients related operations')

ingredients= [
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
class Ingredients(Resource):
    @api.doc('list_ingredients')
    def get(self):
        '''List all ingredients'''
        return ingredients

@api.route('/<id>')
@api.param('id', 'The ingredient identifier')
@api.response(404, 'Ingredient not found')
class Ingredient(Resource):
    @api.doc('get_ingredient')
    def get(self, id):
        '''Fetch an ingredient given its identifier'''
        for ingredient in ingredients:
            if ingredient['id'] == id:
                return ingredient
        api.abort(404)