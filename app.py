from flask import Flask
from apis import api
from core.db import init_db, backup_db
from core.errors import DbConnectError

def init_settings():
    try:
        init_db()
    except DbConnectError as e:
        print(e)


def create_app():
    app = Flask(__name__)
    api.init_app(app)
    init_settings()

    backup_db()

    return app