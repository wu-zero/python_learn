from conf import settings
import logging
import logging.config
import json


def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(name)  # 生成一个log实例
    return logger


def conn_db():
    db_path = settings.DB_PATH
    dic = json.load(open(db_path, 'r', encoding='utf-8'))
    return dic

def save_db(dic):
    db_path = settings.DB_PATH
    json.dump(dic, open(db_path, 'w', encoding='utf-8'))
