from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import config


db = SQLAlchemy()


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))

    # load extensions
    db.init_app(app)
    CORS(app)
    JWTManager(app)
    api = Api(app)

    from app import routes

    routes.load(api)

    return app
