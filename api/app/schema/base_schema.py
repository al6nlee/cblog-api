from marshmallow import Schema, EXCLUDE, fields, post_load

from api.app.utils.response import BaseResponse, SuccessResponse


class RawBaseSchema(Schema):
    class Meta:
        strict = True
        datetimeformat = "%Y-%m-%d %H:%M:%S"
        unknown = EXCLUDE  # 排除未知字段


class BaseResponseSchema(RawBaseSchema):
    code = fields.Integer(default=SuccessResponse.Code)
    message = fields.String(default=SuccessResponse.Message)


class BaseResponseItemSchema(BaseResponseSchema):
    item = fields.Raw(description="数据")


class BaseResponseItemsSchema(BaseResponseSchema):
    items = fields.List(fields.Raw(), description="数据")
    total = fields.Integer(description="总数")


class PaginationSchema(RawBaseSchema):
    """分页参数"""
    page = fields.Integer(description="页码", missing=1, default=1)
    per_page = fields.Integer(description="每页数量", missing=10, default=10)


class BaseResponsePaginationSchema(PaginationSchema, BaseResponseItemsSchema):
    items = fields.List(fields.Raw(), description="数据")
    total = fields.Integer(description="总数")
