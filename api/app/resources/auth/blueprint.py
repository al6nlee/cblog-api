from api.app.initialization import smorest_api
from api.app.resources.base_blueprint import Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix="/auth", description='权限相关')


def register_auth_bp():
    from api.app.resources.auth.resource_user import UserResource
    from api.app.resources.auth.resource_user import UserListResource

    auth_bp.add_resource(UserResource, '/user/<int:user_id>')
    auth_bp.add_resource(UserListResource, '/user')

    smorest_api.register_blueprint(auth_bp)
