from api.app.initialization import db
from api.app.model.base import BaseModel


class Category(BaseModel):
    __tablename__ = 'tbl_category'

    name = db.Column(db.String(100), nullable=True, comment='分类名称')
