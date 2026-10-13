# 该脚本用于: 文本预处理.
import jieba
from base import logger

def preprocess(text):
    """文本预处理"""
    try:
        # 使用jieba进行分词
        seg_list = jieba.lcut(text.lower())
        
        return seg_list
    except Exception as e:
        logger.error(f"文本预处理失败: {e}")
        return []
