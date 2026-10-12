""" 
该脚本用于: MySQL数据库的基础操作. 
"""

import pymysql
import pandas as pd
import sys,os

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取模块目录
module_dir = os.path.dirname(current_dir)

# 获取项目根目录
project_dir = os.path.dirname(module_dir)

# 将项目根目录添加到系统路径
sys.path.append(project_dir)

from base import config,logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 创建引擎
engine = create_engine(
    f"mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}:{config.MYSQL_PORT}/{config.MYSQL_DATABASE}",
    echo=False,   # 是否但因sql用于调试
    pool_recycle=3600,   # 防止mysql 8小时断连
    pool_pre_ping=True,   # 连接池心跳检测
)

# 创建session工厂
SessionLocal = sessionmaker(bind=engine)

# 提供一个获取session的上下文管理器,确保session用完自动关闭
from contextlib import contextmanager

@contextmanager
def get_db_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error("数据库操作失败: {}".format(e))
        raise
    finally:
        session.close()
