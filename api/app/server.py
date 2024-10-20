import warnings
from flask import Flask
from api.app.initialization import register_extension
from api.app.initialization.handler import register_handler
from api.app.initialization.middleware import register_middleware
from api.app.config import Config


def create_app():
    _app = Flask(__name__)
    _app.config.from_object(Config)

    warnings.filterwarnings(
        # 在一些场景下(比如UserSchema(partial=True) 和 UserSchema就被被解析出相同的名称User)，会出现Multiple schemas resolved to the name的警告，忽略掉
        "ignore",
        message="Multiple schemas resolved to the name",
    )

    register_extension(_app)

    register_handler(_app)

    from api.app.initialization.cli import register_cli
    register_cli(_app)

    from api.app.resources.registry import register_resource
    register_resource()

    register_middleware(_app)

    return _app


server_app = create_app()
