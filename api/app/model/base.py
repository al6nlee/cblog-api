from datetime import datetime

from api.app.initialization import db


class BaseModel(db.Model):
    __abstract__ = True  # 使这个类不会创建一个表

    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"
