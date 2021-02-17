from flask_restplus import Api

from .articles import api as articles
from .comments import api as comments
from .ingredients import api as ingredients
from .logs import api as logs
from .sessions import api as sessions
from .users import api as users

api = Api(
    title='My Title',
    version='1.0',
    description='A description',
)

api.add_namespace(articles)
api.add_namespace(comments)
api.add_namespace(ingredients)
api.add_namespace(logs)
api.add_namespace(sessions)
api.add_namespace(users)