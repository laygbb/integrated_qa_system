# 该脚本主要用于配置 base包下的脚本文件, 怎么导, 具体用谁等信息.


# 导包
import os       # 用于处理文件路径的
import sys      # 用于管理python解释器的系统路径(sys.path), 即: 确保自定义的模块能被正确导入

# 1. 获取当前文件所在的目录的绝对路径.
module_dir = os.path.dirname(os.path.abspath(__file__))
# print(f'module_dir: {module_dir}')      # D:\workspace\ai_34_bj\integrated_qa_system\base

# 2. 获取项目根目录的绝对路径.
project_root = os.path.dirname(module_dir)
# print(f'project_root: {project_root}')    # D:\workspace\ai_34_bj\integrated_qa_system

# 3. 将模块目录添加到 系统路径 -> 即: sys.path
# 逻辑: 若模块目录不再sys.path中, 则插入到列表首位, 即: 优先加载当前模块目录下的文件, 避免同名模块冲突.
if module_dir not in sys.path:
    sys.path.insert(0, module_dir)

# 4. 将项目目录添加到 系统路径 -> 即: sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# 5. 测试是否添加成功.
# print(sys.path)


# 6. 导入自定义模块 -> 依赖上述的路径配置, 确保能找到 config.py 和 logger.py
from config import config
from logger import logger