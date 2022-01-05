from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    from app.image.controllers import image_mod

    app.register_blueprint(image_mod)

    return app
