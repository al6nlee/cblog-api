from flask import Blueprint, Flask
from flask_restful import Api

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
auth_api = Api(auth_bp)  # 将 API 对象与蓝图关联


def register_auth_bp(app_: Flask):
    # auth_api.add_resource(UserResource, '/user')
    app_.register_blueprint(auth_bp)
