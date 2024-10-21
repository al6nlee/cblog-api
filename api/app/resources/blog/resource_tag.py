from flask_restful import Resource
from api.app.resources.auth.blueprint import auth_bp
from api.app.schema.base_schema import BaseResponseItemsSchema
from api.app.utils.response import SuccessResponse


class BlogTagListResource(Resource):
    @auth_bp.response(200, BaseResponseItemsSchema)
    def get(self):
        """获取所有分类"""
        tag_list = [
            {"id": 1, "name": "并发编程"},
            {"id": 2, "name": "面试题"},
            {"id": 3, "name": "系统架构"},
        ]
        total, items = len(tag_list), tag_list
        return SuccessResponse().set_items(items, total)
