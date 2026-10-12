# 该脚本用于: 日志设置.


import logging
from config import config
import os


# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)

# 获取当前文件的目录路径
current_dir_path = os.path.dirname(current_file_path)

# 获取项目根目录路径
project_root_path = os.path.dirname(current_dir_path)

# 配置文件路径
log_file_path = os.path.join(config.LOG_PATH, 'logs', config.LOG_FILE_NAME)

# 封装log日志配置函数
def setup_logger(log_file_path=log_file_path):
    
    # 获取日志所在目录，如果目录不存在则创建
    if not os.path.exists(os.path.dirname(log_file_path)):
        os.makedirs(os.path.dirname(log_file_path))
    
    log_dir = os.path.dirname(log_file_path)
    
    # 创建一个日志记录器
    logger = logging.getLogger("integrated_qa_system")
    logger.setLevel(config.LOG_LEVEL)

    # 创建一个handler，用于写入日志文件
    log_file_path = os.path.join(config.LOG_PATH, 'logs', config.LOG_FILE_NAME)
    fh = logging.FileHandler(log_file_path)
    fh.setLevel(config.LOG_LEVEL)

    # 创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(config.LOG_LEVEL)

    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger

logger = setup_logger()