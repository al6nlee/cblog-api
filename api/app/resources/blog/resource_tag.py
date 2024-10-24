from flask_restful import Resource
from api.app.resources.auth.blueprint import auth_bp
from api.app.schema.base_schema import BaseResponseItemsSchema
from api.app.utils.response import SuccessResponse


class BlogTagListResource(Resource):
    @auth_bp.response(200, BaseResponseItemsSchema)
    def get(self):
        """获取所有标签及其包含的博客"""
        tag_list = [
            {"id": 1, "name": "并发编程", "blog_list": [{"title": "01-并发编程入门", "update_date": "2020-01-01"},
                                                        {"title": "02-并发编程进阶", "update_date": "2020-01-01"},
                                                        {"title": "03-并发编程入门", "update_date": "2020-01-01"},
                                                        {"title": "04-并发编程进阶", "update_date": "2020-01-01"},
                                                        {"title": "05-并发编程入门", "update_date": "2020-01-01"},
                                                        {"title": "06-并发编程进阶", "update_date": "2020-01-01"},
                                                        {"title": "07-并发编程入门", "update_date": "2020-01-01"},
                                                        {"title": "08-并发编程进阶", "update_date": "2020-01-01"},
                                                        {"title": "09-并发编程入门", "update_date": "2020-01-01"},
                                                        {"title": "10-并发编程进阶", "update_date": "2020-01-01"}],
             "blog_num": 10},
            {"id": 2, "name": "面试题", "blog_list": [{"title": "01-面试题入门", "update_date": "2020-01-01"}],
             "blog_num": 1},
            {"id": 3, "name": "系统架构", "blog_list": [{"title": "01-系统架构入门", "update_date": "2020-01-01"}],
             "blog_num": 1},
        ]
        total, items = len(tag_list), tag_list
        return SuccessResponse().set_items(items, total)
