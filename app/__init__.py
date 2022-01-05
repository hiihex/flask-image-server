from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    from app.models import db
    db.init_app(app)

    return app
