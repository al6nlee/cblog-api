from api.app.initialization import db
from api.app.model.base import BaseModel


class User(BaseModel):
    __tablename__ = 'tbl_user'

    username = db.Column(db.String(100), nullable=False, unique=True, comment='用户名')
    nickname = db.Column(db.String(50), nullable=True, comment='昵称')
    password = db.Column(db.String(200), nullable=False, comment='用户密码')
    phone_number = db.Column(db.String(20), nullable=True, unique=True, comment='手机号')
    email = db.Column(db.String(200), nullable=False, unique=True, comment='用户邮箱')
    role_id = db.Column(db.Integer, nullable=False, comment='角色ID')
    gender = db.Column(db.String(10), nullable=True, comment='性别')
    location = db.Column(db.String(100), nullable=True, comment='位置/地址')
    birthdate = db.Column(db.Date, nullable=True, comment='出生日期')
    avatar = db.Column(db.String(200), nullable=True, comment='头像URL')
    signature = db.Column(db.String(200), nullable=True, default="这个人很懒，什么都没留下！", comment='个性签名')
