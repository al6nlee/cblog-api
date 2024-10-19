from flask_smorest import abort
from flask_restful import Resource
from api.app.resources.auth.blueprint import auth_bp
from api.app.schema.base_schema import BaseResponseItemSchema, BaseResponsePaginationSchema, PaginationSchema
from api.app.service.auth.service_user import user_service
from api.app.schema.auth.schema_user import UserSchema
from api.app.utils.response import SuccessResponse


class UserListResource(Resource):
    @auth_bp.arguments(PaginationSchema, location="query")
    @auth_bp.response(200, BaseResponsePaginationSchema)
    def get(self, args):
        """获取用户列表"""
        total, items = user_service.get_users_list(args)
        return SuccessResponse().set_items(items, total)

    @auth_bp.arguments(UserSchema)  # 装饰器处理数据效验和解析
    @auth_bp.response(201, UserSchema)
    def post(self, user_data):
        """创建新用户，user_data 是已经效验通过的数据"""
        return user_service.create_user(user_data)


class UserResource(Resource):
    @auth_bp.response(200, BaseResponseItemSchema)
    def get(self, user_id):
        """根据用户ID获取用户"""
        item = user_service.get_user(user_id)
        return SuccessResponse().set_item(item)

    @auth_bp.arguments(UserSchema(partial=True))  # 允许部分更新
    @auth_bp.response(200, UserSchema)
    def put(self, updated_user_data, user_id):
        """根据用户ID更新用户"""
        updated_user = user_service.update_user(user_id, updated_user_data)
        if updated_user is None:
            abort(404, message="用户不存在")
        return updated_user

    @auth_bp.response(204, UserSchema)
    def delete(self, user_id):
        """根据用户ID删除用户"""
        if not user_service.delete_user(user_id):
            abort(404, message="用户不存在")
        return '', 204
