from datetime import datetime, date

from sqlalchemy import select, Table, MetaData, create_engine
from sqlalchemy_utils import database_exists, create_database
from api.app.utils.driver import logger

# 获取当前时间
current_time = datetime.now()


def ensure_database_exists(config):
    """检查数据库是否存在，如果不存在则创建"""
    url = config.get_main_option("sqlalchemy.url")
    engine = create_engine(url)

    if not database_exists(engine.url):
        logger.info(f"Database does not exist. Creating database at {url}...")
        create_database(engine.url, encoding="utf8mb4")
        logger.info("Database created successfully!")
    else:
        logger.info(f"Database already exists at {url}.")


def initialize_project_data(connection):
    """初始化项目必要的表数据，如果表是空的则插入数据"""

    metadata = MetaData()
    metadata.reflect(bind=connection)

    # tbl_user 表初始化
    tbl_user = Table('tbl_user', metadata, autoload_with=connection)
    if is_table_empty(connection, tbl_user):
        connection.execute(tbl_user.insert(), [
            {"id": 1, "username": "admin", "email": "admin@example.com", "password": "admin123", "role_id": 1,
             "gender": "male", "location": "中国-北京市-北京市", "birthdate": date(2000, 1, 1),
             "avatar": "avatar-8c6976e5b5.png", "signature": "这个人很懒，什么都没留下！", "phone_number": "1234567891",
             "create_date": current_time, "update_date": current_time},
            {"id": 2, "username": "alan", "email": "alan@example.com", "password": "user123", "role_id": 2,
             "gender": "female", "location": "中国-上海市-上海市", "birthdate": date(2000, 1, 1),
             "avatar": "avatar-db42328112.png", "signature": "这个人很懒，什么都没留下！", "phone_number": "1234567892",
             "create_date": current_time, "update_date": current_time},
        ])
        logger.info("Initialized tbl_user data")

    # tbl_role 表初始化
    tbl_role = Table('tbl_role', metadata, autoload_with=connection)
    if is_table_empty(connection, tbl_role):
        connection.execute(tbl_role.insert(), [
            {"id": 1, "name": "管理员", "create_date": current_time, "update_date": current_time},
            {"id": 2, "name": "普通用户", "create_date": current_time, "update_date": current_time},
        ])
        logger.info("Initialized tbl_role data")

    connection.commit()
    logger.info("Initialized project data successfully!")


def is_table_empty(connection, table):
    result = connection.execute(select(table)).fetchone()  # 直接传递表对象
    return result is None
