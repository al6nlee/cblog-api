from api.app.initialization import db
from api.app.model.base import BaseModel


class Role(BaseModel):
    __tablename__ = 'tbl_role'  # 设置表名
    __table_args__ = {'extend_existing': True}
    name = db.Column(db.String(100), nullable=False, unique=True)  # 角色名称
