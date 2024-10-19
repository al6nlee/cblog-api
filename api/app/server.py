from flask import Flask

from api.app.initialization import db, register_extension
from api.app.initialization.middleware import register_middleware
from api.app.config import Config
from api.app.utils.driver import logger
from sqlalchemy_utils import database_exists, create_database


def create_app():
    _app = Flask(__name__)
    logger.info("加载配置信息")
    _app.config.from_object(Config)

    db.init_app(_app)

    logger.info("加载路由")
    from api.app.resources.registry import register_resource
    register_resource(_app)
    register_extension(_app)

    logger.info("加载中间件")
    register_middleware(_app)

    return _app


server_app = create_app()
