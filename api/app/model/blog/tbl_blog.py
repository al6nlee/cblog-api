from api.app.initialization import db
from api.app.model.base import BaseModel


class Blog(BaseModel):
    __tablename__ = 'tbl_blog'

    title = db.Column(db.String(200), nullable=False, comment='博客标题')
    abstract = db.Column(db.String(1024), nullable=False, comment='摘要')
    category_id = db.Column(db.Integer, nullable=True, comment='分类ID')
    author_id = db.Column(db.Integer, nullable=False, comment='作者ID')
    is_draft = db.Column(db.Boolean, default=True, comment='是否为草稿')
    detail_id = db.Column(db.Integer, nullable=True, comment='详情内容ID')

class BlogTags(db.Model):
    __tablename__ = 'tbl_blog_tags'

    blog_id = db.Column(db.Integer, primary_key=True, comment='博客ID')
    tag_id = db.Column(db.Integer, primary_key=True, comment='标签ID')
