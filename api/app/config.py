import os

PROJECT_ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))  # 项目绝对路径
DEBUG_MODE = os.getenv("DEBUG_MODE", False)
HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", 50001)


class Config:
    DEBUG = DEBUG_MODE
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{PROJECT_ROOT_PATH}/api/data/api.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
