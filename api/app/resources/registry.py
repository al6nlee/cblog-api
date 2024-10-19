from api.app.resources.auth.blueprint import register_auth_bp
from api.app.resources.blog.blueprint import register_blog_bp
from api.app.resources.check import register_health_bp


def register_resource():
    register_health_bp()
    register_auth_bp()
    register_blog_bp()
