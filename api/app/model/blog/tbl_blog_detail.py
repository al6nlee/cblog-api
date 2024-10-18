from api.app.initialization import db


class BlogDetail(db.Model):
    __tablename__ = 'tbl_blog_detail'

    id = db.Column(db.Integer, primary_key=True, comment='主键ID')
    blog_id = db.Column(db.Integer, nullable=False, unique=True, comment='博客ID，唯一，关联博客表')
    abstract = db.Column(db.String(500), comment='博客摘要')
    content = db.Column(db.Text, nullable=False, comment='博客内容')
