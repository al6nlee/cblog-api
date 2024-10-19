from api.app.initialization import db
from api.app.model.auth.tbl_user import User


class UserService:

    def create_user(self, validated_data):
        """创建新用户"""
        new_user = User(**validated_data)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_user(self, user_id):
        """根据ID获取用户"""
        return db.session.query(User).get(user_id)

    def update_user(self, user_id, validated_data):
        """更新用户"""
        user = db.session.query(User).get(user_id)
        if not user:
            return None
        for key, value in validated_data.items():
            setattr(user, key, value)
        db.session.commit()
        return user

    def delete_user(self, user_id):
        """删除用户"""
        user = db.session.query(User).get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

    def get_all_users(self):
        """获取所有用户"""
        return db.session.query(User).all()


user_service = UserService()
