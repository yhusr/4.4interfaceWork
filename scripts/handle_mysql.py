import pymysql
import random
from scripts.handle_conf import hy


class HandleMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host=hy.read_yaml('mysql', 'host'),
            user=hy.read_yaml('mysql', 'user'),
            password=hy.read_yaml('mysql', 'password'),
            charset='utf8',
            db=hy.read_yaml('mysql', 'db'),
            cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    @staticmethod
    def random_phone():
        return hy.read_yaml('phone', 'prefixes') + ''.join(random.sample('0123456789', 8))

    # 查询数据中的数据：如13420835259,
    # hy.read_yaml('mysql', 'sql')
    def get_result(self, sql, args=None, size=1, fetchone=True):
        # result_sql = None
        self.cursor.execute(sql, args)
        self.conn.commit()
        if fetchone:
            result_sql = self.cursor.fetchone()
        else:
            if isinstance(size, int):
                if size >= 0:
                    result_sql = self.cursor.fetchmany(size=size)
                else:
                    result_sql = self.cursor.fetchall()
            else:
                print(f'此查询长度{size}输入错误')
        return result_sql

    def no_result_boolean(self, sql, args=None):
        result = self.get_result(sql=sql, args=args)
        if result:
            return False
        else:
            return True

    def no_exists_phone(self):
        sql = hy.read_yaml('mysql', 'sql')
        while True:
            phone = HandleMysql.random_phone()
            result = self.no_result_boolean(sql=sql, args=phone)
            if result:
                break
        return phone

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    hm = HandleMysql()
    result = hm.get_result(hy.read_yaml('mysql', 'sql'), '14336298507')
    hm.close()
    print(result)
    # phone = hm.no_exists_result()
    # print(phone)