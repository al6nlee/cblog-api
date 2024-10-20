from api.app.initialization import db
from api.app.model.base import BaseModel


class Role(BaseModel):
    __tablename__ = 'tbl_role'

    name = db.Column(db.String(100), nullable=False, unique=True, comment='角色名称')
    description = db.Column(db.String(255), nullable=True, comment='角色描述')
