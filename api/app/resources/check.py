from api.app.initialization import smorest_api
from api.app.resources.base_blueprint import Blueprint
from flask_restful import Resource


class HealthCheck(Resource):
    def get(self):
        return {'status': 'healthy'}, 200


check_bp = Blueprint('check', __name__, url_prefix='/check', description='健康检查')


def register_health_bp():
    check_bp.add_resource(HealthCheck, '')
    smorest_api.register_blueprint(check_bp)
