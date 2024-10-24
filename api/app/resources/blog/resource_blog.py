from flask_restful import Resource
from api.app.resources.blog.blueprint import blog_bp
from api.app.schema.base_schema import BaseResponseItemSchema
from api.app.utils.response import SuccessResponse


class BlogDetailResource(Resource):

    @blog_bp.response(200, BaseResponseItemSchema)
    def get(self, id):
        """根据分类ID获取指定分类下的博客信息"""
        item = {
            "title": f"我是一篇博客{id}", "abstract": "python并发编程", "author": "alan",
            "create_date": "2020-01-01", "update_date": "2024-01-01", "tags": ["开发", "python"],
            "views": 12345, "likes": 567, "comments": 89, "content": "# 标题一\n\n> 我是内容"
        }
        return SuccessResponse().set_item(item)
