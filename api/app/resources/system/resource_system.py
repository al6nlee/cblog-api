from flask_restful import Resource
from api.app.resources.system.blueprint import system_bp
from api.app.schema.base_schema import BaseResponseItemSchema
from api.app.utils.response import SuccessResponse


class SystemConfigResource(Resource):
    @system_bp.response(200, BaseResponseItemSchema)
    def get(self):
        """获取系统配合信心"""
        system_config = {
            "name": "文斋阁",
            "logo": "/favicon.ico",
        }
        return SuccessResponse().set_item(system_config)
