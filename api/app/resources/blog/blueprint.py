from flask import Blueprint, Flask
from flask_restful import Api

blog_bp = Blueprint("blog", __name__, url_prefix="/blog")
blog_api = Api(blog_bp)


def register_blog_bp(app_: Flask):
    # blog_api.add_resource(BlogListResource, '/list')
    app_.register_blueprint(blog_bp)
