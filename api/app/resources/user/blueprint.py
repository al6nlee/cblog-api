from flask import Blueprint, Flask

user_bp = Blueprint("user", __name__, url_prefix="/user")


def register_user_bp(app_: Flask):
    app_.register_blueprint(user_bp)
