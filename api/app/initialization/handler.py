from flask import jsonify

from api.app.utils.driver import logger
from api.app.utils.response import BaseResponse


def register_handler(app):
    @app.errorhandler(Exception)
    def err_not_catch(err: Exception):
        logger.exception(str(err))
        response = {
            "code": BaseResponse.Code,
            "message": BaseResponse.Message
        }
        return jsonify(response), 500
