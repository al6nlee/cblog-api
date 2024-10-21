from api.app.initialization import smorest_api
from api.app.resources.base_blueprint import Blueprint

blog_bp = Blueprint("blog", __name__, url_prefix="/blog", description="博客相关")


def register_blog_bp():
    from api.app.resources.blog.resource_category import BlogCategoryListResource
    from api.app.resources.blog.resource_tag import BlogTagListResource
    blog_bp.add_resource(BlogCategoryListResource, '/category')
    blog_bp.add_resource(BlogTagListResource, '/tag')
    smorest_api.register_blueprint(blog_bp)
