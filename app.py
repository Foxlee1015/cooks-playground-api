from flask import Flask
from apis import api
from core.db import init_db

app = Flask(__name__)
api.init_app(app)
init_db()