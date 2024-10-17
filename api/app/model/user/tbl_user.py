from api.app.initialization import db
from api.app.model.base import BaseModel


class User(BaseModel):
    __tablename__ = 'tbl_user'
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    role_id = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    birthdate = db.Column(db.Date, nullable=True)
    avatar = db.Column(db.String(200), nullable=True)
    avatar1 = db.Column(db.String(200), nullable=True)
    avatar2 = db.Column(db.String(200), nullable=True)
    signature = db.Column(db.String(200), nullable=True, default="这个人很懒，什么都没留下！")


class Role(BaseModel):
    __tablename__ = 'tbl_role'  # 设置表名
    name = db.Column(db.String(100), nullable=False, unique=True)  # 角色名称
