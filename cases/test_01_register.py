import unittest
from libs.ddt import data,ddt
from scripts.handle_excel import HandleExcel
from scripts.handle_request import HandleRequest
from scripts.handle_mysql import HandleMysql
from scripts.handle_re import HandleRe as hre
from scripts.handle_conf import hy
from scripts.handle_log import my_logger


@ddt
class TestRegister(unittest.TestCase):
    he = HandleExcel('register')
    ex_data = he.read_excel()

    @classmethod
    def setUpClass(cls) -> None:
        cls.hr = HandleRequest()
        cls.hm = HandleMysql()

    @data(*ex_data)
    def test_register(self, ex_data):
        title = ex_data.title
        base_url = hy.read_yaml('api', 'load')
        request_url = ''.join((base_url, ex_data.url))
        head = hy.read_yaml('api', 'header')
        phone = self.hm.no_exists_phone()
        json_re = hre.re_data(re_args=phone, data=ex_data.data)
        self.hr.common_headers(head)
        result = self.hr.send(url=request_url, data=json_re)
        result_json = result.json()
        try:
            self.assertListEqual([result_json.get('code'), result_json.get('msg')],
                                 [ex_data.expected, ex_data.msg], msg=f'用例{title}结果验证')
        except AssertionError as e:
            self.he.write_excel(int(ex_data.caseId) + 1, 7, 'fail')
            my_logger.error(f'用例{title}验证失败,错误信息如下{e}')
        else:
            self.he.write_excel(int(ex_data.caseId) + 1, 7, 'success')
            my_logger.info(f'用例{title}验证通过')
        finally:
            self.he.write_excel(int(ex_data.caseId) + 1, 8, result.text)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.hr.close()
        cls.hm.close()
