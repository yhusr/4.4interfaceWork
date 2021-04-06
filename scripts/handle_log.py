import logging
from scripts.handle_os import LOG_PATH
import time
import os


class HandleLog:

    @staticmethod
    def get_logger():
        logger = logging.getLogger("mytest")
        fom = '%(asctime)s - %(name)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        logging.Formatter(fom)

        # 控制台输出
        sh = logging.StreamHandler()
        logger.setLevel('DEBUG')
        logger.addHandler(sh)

        # 文件输出
        time_str = time.strftime('%Y%d%m%H%M%S', time.localtime(time.time()))
        fh = logging.FileHandler(filename=os.path.join(LOG_PATH, f'test_{time_str}.log'),
                                 encoding='utf-8')
        logger.setLevel('DEBUG')
        logger.addHandler(fh)

        return logger


my_logger = HandleLog.get_logger()

