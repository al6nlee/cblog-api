from api.app.initialization import smorest_api
from api.app.resources.base_blueprint import Blueprint

system_bp = Blueprint("system", __name__, url_prefix="/system", description="系统相关")


def register_system_bp():
    from api.app.resources.system.resource_system import SystemConfigResource
    system_bp.add_resource(SystemConfigResource, '/config')
    smorest_api.register_blueprint(system_bp)
