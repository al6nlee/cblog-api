from api.app.initialization import db


class BlogDetail(db.Model):
    __tablename__ = 'tbl_blog_detail'
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, nullable=False, unique=True)
    abstract = db.Column(db.String(500))
    content = db.Column(db.Text, nullable=False)
