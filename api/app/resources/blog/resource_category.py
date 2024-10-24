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


class BlogCategoryResource(Resource):

    @blog_bp.response(200, BaseResponseItemsSchema)
    def get(self, id):
        """根据分类ID获取指定分类下的博客信息"""
        items = [
            {"id": 1, "title": "01-入门", "abstract": "python并发编程", "author": "zhangsan",
             "create_date": "2020-01-01", "update_date": "2024-01-01", "tags": ["开发", "编程"],
             "views": 12345, "likes": 567, "comments": 89},
            {"id": 2, "title": "01-高级", "abstract": "python并发编程", "author": "zhangsan",
             "create_date": "2020-01-01", "update_date": "2024-01-01", "tags": ["开发"],
             "views": 22, "likes": 111, "comments": 2},
        ]
        total = len(items)
        return SuccessResponse().set_items(items, total)
