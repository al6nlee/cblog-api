from flask_restful import Resource
from api.app.resources.blog.blueprint import blog_bp
from api.app.schema.base_schema import BaseResponseItemsSchema, BaseResponseItemSchema
from api.app.utils.response import SuccessResponse


class BlogHotResource(Resource):
    @blog_bp.response(200, BaseResponseItemsSchema)
    def get(self):
        """获取热门博客列表"""
        category_list = [
            {"id": 1, "title": "python开发入门"},
            {"id": 2, "name": "java开发入门"}
        ]
        total, items = len(category_list), category_list
        return SuccessResponse().set_items(items, total)
