from flask_restful import Resource
from api.app.resources.blog.blueprint import blog_bp
from api.app.schema.base_schema import BaseResponseItemsSchema, BaseResponseItemSchema
from api.app.utils.response import SuccessResponse


class BlogCategoryListResource(Resource):
    @blog_bp.response(200, BaseResponseItemsSchema)
    def get(self):
        """获取所有分类"""
        category_list = [
            {"id": 1, "name": "python"},
            {"id": 2, "name": "java"},
            {"id": 3, "name": "go"},
            {"id": 4, "name": "c++"},
        ]
        total, items = len(category_list), category_list
        return SuccessResponse().set_items(items, total)
