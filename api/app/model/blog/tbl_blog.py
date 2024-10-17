from api.app.initialization import db
from api.app.model.base import BaseModel


class Blog(BaseModel):
    __tablename__ = 'tbl_blog'
    title = db.Column(db.String(200), nullable=False)
    category_id = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer, nullable=False)
    is_draft = db.Column(db.Boolean, default=True)
    detail_id = db.Column(db.Integer, nullable=True)


class BlogTags(db.Model):
    __tablename__ = 'tbl_blog_tags'
    blog_id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, primary_key=True)
