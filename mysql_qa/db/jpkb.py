from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Table, Boolean
from sqlalchemy.orm import declarative_base

import pandas as pd
from mysql_client import get_db_session

Base = declarative_base()

class JPKB(Base):
    __tablename__ = 'jpkb'

    id = Column(Integer, primary_key=True)
    subject_name = Column(String(20))
    question = Column(String(1000))
    answer = Column(String(1000))
    
    def from_dict(self,data):
        self.subject_name = data['subject_name']
        self.question = data['question']
        self.answer = data['answer']
        
    def to_dict(self):
        return {
            'id': self.id,
            'subject_name': self.subject_name,
            'question': self.question,
            'answer': self.answer
        }
    

def get_batch_data_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    
    with get_db_session() as session:
        for _, row in df.iterrows():
            jpkb = JPKB()
            row['subject_name'], row['question'], row['answer'] =  row['学科名称'], row['问题'], row['答案']
            jpkb.from_dict(row)
            session.add(jpkb)
    
    
def fetch_answer(question):
    """根据指定问题,从数据库中查询答案"""
    
    try:
        with get_db_session() as session:
            jpkb = session.query(JPKB).filter(JPKB.question == question).first()
            if jpkb:
                return jpkb.answer
            else:
                return None
    except Exception as e:
        logger.error(f"根据问题查询答案失败: {e}")
        return None
        
    
if __name__ == '__main__':
    # get_batch_data_from_csv('D:\AI_project\integrated_qa_system\mysql_qa\data\JP学科知识问答.csv')
    
    query = '用上下文管理器实现函数运行时间的计算?'
    answer = fetch_answer(query)
    print(answer)