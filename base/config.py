# 该脚本用于: 配置文件管理. 

import os
import configparser

# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)

# 获取当前文件的目录路径
current_dir_path = os.path.dirname(current_file_path)

# 获取项目根目录路径
project_root_path = os.path.dirname(current_dir_path)

# 配置文件路径
config_file_path = os.path.join(project_root_path, 'config.ini')

# 配置解析类
class Config:
    def __init__(self):
        """ 初始化配置,加载config.ini文件，并解析各服务的配置参数."""
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path, encoding='utf-8')
        
        # MySQL配置
        self.MYSQL_HOST = self.config.get('mysql', 'host',fallback='localhost')
        self.MYSQL_PORT = self.config.getint('mysql', 'port',fallback=3306)
        self.MYSQL_USER = self.config.get('mysql', 'user',fallback='root')
        self.MYSQL_PASSWORD = self.config.get('mysql', 'password',fallback='123456')
        self.MYSQL_DATABASE = self.config.get('mysql', 'database',fallback='test')
        
        # REDIS配置
        self.REDIS_HOST = self.config.get('redis', 'host',fallback='localhost')
        self.REDIS_PORT = self.config.getint('redis', 'port',fallback=6379)
        self.REDIS_PASSWORD = self.config.get('redis', 'password')
        self.REDIS_DB = self.config.getint('redis', 'db',fallback=0)
        
        # MILVUS配置
        self.MILVUS_HOST = self.config.get('milvus', 'host',fallback='localhost')
        self.MILVUS_PORT = self.config.getint('milvus', 'port',fallback=19530)
        
        
        # log日志
        self.LOG_PATH = self.config.get('log', 'path')
        self.LOG_FILE_NAME = self.config.get('log', 'file_name',fallback='log.log')
        self.LOG_LEVEL = self.config.get('log', 'level',fallback='INFO')
        
config = Config()
# print(config.MYSQL_HOST)