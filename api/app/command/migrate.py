from datetime import datetime, date

from flask import current_app
from flask.cli import AppGroup
from sqlalchemy_utils import database_exists, create_database

from api.app.initialization import session
from api.app.model.auth.tbl_role import Role
from api.app.model.auth.tbl_user import User
from api.app.utils.driver import logger

migrate = AppGroup("migrate")


@migrate.command("create-db")
def create_db():
    """
    Create database if it doesn't exist.
    """

    logger.info(f"Check if the database {current_app.config['DB_NAME']} exists ...")
    if database_exists(current_app.config["SQLALCHEMY_DATABASE_URI"]):
        logger.info(f"Database {current_app.config['DB_NAME']} already exists, skipping creation.")
    else:
        logger.info(f"Database {current_app.config['DB_NAME']} does not exist, creating it ...")
        create_database(current_app.config["SQLALCHEMY_DATABASE_URI"], encoding="utf8mb4")
        logger.info("Database created successfully!")


@migrate.command('init-db')
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
