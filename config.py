import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "some-secret-key"
    JWT_SECRET_KEY = "jwt-secret-string"
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]


class Development(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "dev.sqlite3")


class Production(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://docker:docker@db/financial_viewer"


config = dict(development=Development, production=Production)
