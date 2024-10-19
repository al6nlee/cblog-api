from api.app.initialization import smorest_api
from api.app.resources.base_blueprint import Blueprint

blog_bp = Blueprint("blog", __name__, url_prefix="/blog", description="博客相关")


def register_blog_bp():
    # blog_bp.add_resource(BlogListResource, '/list')
    smorest_api.register_blueprint(blog_bp)
