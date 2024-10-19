import os

PROJECT_ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))  # 项目绝对路径
DEBUG_MODE = os.getenv("DEBUG_MODE", True)
HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", 50001)

# Swagger配置
API_TITLE = os.getenv("API_TITLE", "CloudBlog项目接口文档")
API_VERSION = os.getenv("API_VERSION", "v1")
OPENAPI_VERSION = os.getenv("OPENAPI_VERSION", "3.0.2")
OPENAPI_URL_PREFIX = os.getenv("OPENAPI_URL_PREFIX", '/')  # 定义 JSON 文件和 UI 的基本路径，如果为 None，则不提供文档。默认就是None
OPENAPI_SWAGGER_UI_PATH = os.getenv("OPENAPI_SWAGGER_UI_PATH", '/swagger-ui')  # Swagger UI 页面的路径（相对于基本路径）
OPENAPI_SWAGGER_UI_URL = os.getenv("OPENAPI_SWAGGER_UI_URL",
                                   "https://cdn.jsdelivr.net/npm/swagger-ui-dist/")  # 里面有一些静态文件，用于渲染UI界面


# 数据库配置
class DB_CONFIG:
    DB_TYPE = os.getenv('DB_TYPE', 'sqlite').lower()
    if DB_TYPE == 'mysql':
        DB_USERNAME = os.getenv('DB_USERNAME', 'root')
        DB_PASSWORD = os.getenv('DB_PASSWORD', 'passwd')
        DB_HOST = os.getenv('DB_HOST', 'localhost')
        DB_PORT = os.getenv('DB_PORT', '3306')
        DB_NAME = os.getenv('DB_NAME', 'testdb')
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    elif DB_TYPE == 'sqlite':
        DB_NAME = os.getenv('DB_NAME', f'{PROJECT_ROOT_PATH}/api/data/api.db')
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"
    else:
        raise ValueError(f"数据库类型不支持, TYPE: {DB_TYPE}")


class Config(DB_CONFIG):
    DEBUG = DEBUG_MODE

    API_TITLE = API_TITLE
    API_VERSION = API_VERSION
    OPENAPI_VERSION = OPENAPI_VERSION
    OPENAPI_URL_PREFIX = OPENAPI_URL_PREFIX
    OPENAPI_SWAGGER_UI_PATH = OPENAPI_SWAGGER_UI_PATH
    OPENAPI_SWAGGER_UI_URL = OPENAPI_SWAGGER_UI_URL
