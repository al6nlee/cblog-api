import time
import uuid

from flask import g
from flask import request
from flask_jwt_extended import current_user

from api.app.utils.driver import logger


def register_middleware(app):
    @app.before_request
    def start_timer():
        g.start = time.monotonic()

    @app.before_request
    def create_trace_id():
        g.request_id = str(uuid.uuid4())
        logger.info({"self_request_id": g.request_id, "call_request_id": None})

    @app.after_request
    def log(response):
        try:
            user_id = current_user.user_id if current_user else None
            time_cost = int((time.monotonic() - g.start) * 1000)
            length = response.headers.get("Content-Length", type=int)
            if 'X-Forwarded-For' in request.headers:
                user_ip = request.headers['X-Forwarded-For'].split(',')[0]  # 获取第一个 IP 地址
            else:
                user_ip = request.remote_addr
            logger.info(
                f'User<{user_id}> IP<{user_ip}> {request.method.upper()} "{request.path}" => '
                f"generated {length} bytes in {time_cost} msecs, "
                f"status_code: {response.status_code}, "
                f"mimetype: {response.mimetype}"
            )
        except Exception as err:
            logger.exception(str(err))
        return response
