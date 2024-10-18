from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.session import Session

db = SQLAlchemy()
migrate = Migrate()
session: Session = db.session


def register_extension(app):
    migrate.init_app(app, db)
