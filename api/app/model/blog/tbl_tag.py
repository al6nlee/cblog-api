from api.app.initialization import db
from api.app.model.base import BaseModel


class Tag(BaseModel):
    __tablename__ = 'tbl_tag'

    name = db.Column(db.String(100), nullable=False, comment='标签名称')
