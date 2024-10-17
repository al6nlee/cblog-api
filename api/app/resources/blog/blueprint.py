from flask import Blueprint, Flask

blog_bp = Blueprint("blog", __name__, url_prefix="/blog")


def register_blog_bp(app_: Flask):
    app_.register_blueprint(blog_bp)
