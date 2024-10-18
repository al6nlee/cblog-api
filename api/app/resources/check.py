from flask import Blueprint
from flask_restful import Api, Resource


class HealthCheck(Resource):
    def get(self):
        return {'status': 'healthy'}, 200


check_bp = Blueprint('check', __name__, url_prefix='/check')
check_api = Api(check_bp)  # 将 API 对象与蓝图关联


def register_health_bp(app_):
    check_api.add_resource(HealthCheck, '/')
    app_.register_blueprint(check_bp)
