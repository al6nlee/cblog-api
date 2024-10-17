from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.session import Session
from flask_restful import Api

db = SQLAlchemy()
session: Session = db.session

api = Api()


def register_extension(app):
    api.init_app(app)
    return api
