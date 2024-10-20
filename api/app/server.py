import warnings
from datetime import datetime, date

from flask import Flask
from sqlalchemy_utils import database_exists, create_database

from api.app.initialization import register_extension, session
from api.app.initialization.handler import register_handler
from api.app.initialization.middleware import register_middleware
from api.app.config import Config
from api.app.model.auth.tbl_role import Role
from api.app.model.auth.tbl_user import User

from api.app.utils.driver import logger


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

    from api.app.resources.registry import register_resource
    register_resource()

    register_middleware(_app)

    return _app


server_app = create_app()


@server_app.cli.command("create-db")
def create_db():
    """
    Create database if it doesn't exist.
    """
    logger.info(f"Check if the database {server_app.config['DB_NAME']} exists ...")
    if database_exists(server_app.config["SQLALCHEMY_DATABASE_URI"]):
        logger.info(f"Database {server_app.config['DB_NAME']} already exists, skipping creation.")
    else:
        logger.info(f"Database {server_app.config['DB_NAME']} does not exist, creating it ...")
        create_database(server_app.config["SQLALCHEMY_DATABASE_URI"], encoding="utf8mb4")
        logger.info("Database created successfully!")


@server_app.cli.command('init-db')
def init_db():
    """初始化数据库，插入默认角色和用户数据（仅在表中无数据时）。"""
    current_time = datetime.utcnow()

    # 定义角色数据
    default_roles = [
        Role(
            id=1,
            name="管理员",
            description="默认角色，拥有最高权限的管理员",
            create_date=current_time,
            update_date=current_time
        ),
        Role(
            id=2,
            name="普通用户",
            description="默认角色，普通用户具有基础使用权限",
            create_date=current_time,
            update_date=current_time
        )
    ]

    # 定义用户数据并加密密码
    default_users = [
        User(
            id=1,
            username="admin",
            nickname="管理员",
            email="admin@example.com",
            password="admin123",  # 使用加密算法存储密码
            role_id=1,
            gender="male",
            location="中国-北京市-北京市",
            birthdate=date(2000, 1, 1),
            avatar="avatar-8c6976e5b5.png",
            signature="这个人很懒，什么都没留下！",
            phone_number="1234567891",
            create_date=current_time,
            update_date=current_time
        ),
        User(
            id=2,
            username="alan",
            nickname="艾伦",
            email="alan@example.com",
            password="user123",  # 同样加密密码
            role_id=2,
            gender="female",
            location="中国-上海市-上海市",
            birthdate=date(2000, 1, 1),
            avatar="avatar-db42328112.png",
            signature="这个人很懒，什么都没留下！",
            phone_number="1234567892",
            create_date=current_time,
            update_date=current_time
        )
    ]

    # 开始数据库事务
    try:
        role_count = session.query(Role).count()
        user_count = session.query(User).count()

        if role_count == 0:
            # 批量插入默认角色数据
            session.add_all(default_roles)
            session.commit()
            logger.info("角色表默认数据批量插入成功！")
        else:
            logger.info("角色表已有数据，无需初始化。")

        if user_count == 0:
            # 批量插入默认用户数据
            session.add_all(default_users)
            session.commit()
            logger.info("用户表默认数据批量插入成功！")
        else:
            logger.info("用户表已有数据，无需初始化。")

    except Exception as e:
        session.rollback()  # 事务回滚
        logger.error(f"数据库初始化失败: {str(e)}")
