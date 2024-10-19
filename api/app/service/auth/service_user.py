from api.app.initialization import db
from api.app.model.auth.tbl_user import User
from api.app.schema.auth.schema_user import UserSchema


class UserService:

    def create_user(self, validated_data):
        """创建新用户"""
        new_user = User(**validated_data)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_user(self, user_id):
        """根据ID获取用户"""
        user = db.session.query(User).get(user_id)
        user_schema = UserSchema()
        user_data = user_schema.dump(user)
        return user_data

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

    def get_users_list(self, args):
        """获取用户列表"""
        # 获取分页参数
        page = args['page']
        per_page = args['per_page']

        # 查询数据库，获取分页结果
        pagination = User.query.paginate(page=page, per_page=per_page, error_out=False)
        users = pagination.items

        # 使用 UserSchema 进行序列化
        user_schema = UserSchema(many=True)
        users_data = user_schema.dump(users)

        return pagination.total, users_data


user_service = UserService()
