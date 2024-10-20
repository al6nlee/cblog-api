from flask_smorest import Api as SmorestApi
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.session import Session
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
session: Session = db.session
cors = CORS()

# Flask-Smorest 的 API（用于生成文档和表单效验）
smorest_api = SmorestApi()


def register_extension(app):
    smorest_api.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    cors.init_app(app)
