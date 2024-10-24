from api.app.initialization import smorest_api
from api.app.resources.base_blueprint import Blueprint

blog_bp = Blueprint("blog", __name__, url_prefix="/blog", description="博客相关")


def register_blog_bp():
    from api.app.resources.blog.resource_category import BlogCategoryListResource, BlogCategoryResource
    from api.app.resources.blog.resource_hot import BlogHotResource
    from api.app.resources.blog.resource_blog import BlogDetailResource
    from api.app.resources.blog.resource_tag import BlogTagListResource
    blog_bp.add_resource(BlogCategoryListResource, '/category')
    blog_bp.add_resource(BlogCategoryResource, '/category/<int:id>')
    blog_bp.add_resource(BlogTagListResource, '/tag')
    blog_bp.add_resource(BlogHotResource, '/hot')
    blog_bp.add_resource(BlogDetailResource, '/detail/<int:id>')
    smorest_api.register_blueprint(blog_bp)
