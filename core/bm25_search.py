# 该脚本用于: BM25搜索, 阈值: >= 0.85才会走MySQL系统.

from base import logger
from rank_bm25 import BM25Okapi
from utils.preprocess import preprocess
from mysql_qa.db.mysql_client import get_db_session
from mysql_qa.db.jpkb import fetch_answer
from mysql_qa.cache import redis_client
import numpy as np

class BM25Search(object):
    def __init__(self, corpus, k1=1.5, b=0.75):
        self.corpus = corpus
        self.bm25 = BM25Okapi(corpus, k1=k1, b=b)
        
    def _softmax(self, scores):
        """
        函数功能:对输入的分数进行softmax归一化,输出总和为1的概率分布.
        :param scores: 用户问题和mysql中各个问题的BM25相似度分数
        :return: softmax归一化后的概率分布
        """
        return np.exp(scores) / np.sum(np.exp(scores))

    def search(self, query, threshold=0.85):
        # 先分词 ,分词逻辑和mysql_qa一样
        query = preprocess(query)
        # 查询相似度分数
        scores = self.bm25.get_scores(query)
        # softmax归一化
        softmax_scores = self._softmax(scores)
        # 找到最高相似度对应的索引和分数
        best_index = softmax_scores.argmax()
        best_score = softmax_scores[index]
        # 如果最高相似度分数小于0.85,则不使用mysql系统
        if best_score >= threshold:

            return best_index, best_score
        else:
            return None, None