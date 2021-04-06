import unittest
from scripts.handle_os import CASE_PATH, REPORT_HTML_PATH
from libs.HTMLTestRunnerNew import HTMLTestRunner


class RunCase:

    @staticmethod
    def run_test():
        dis = unittest.defaultTestLoader.discover(CASE_PATH)
        runner = HTMLTestRunner(stream=open(file=REPORT_HTML_PATH, mode='wb'),
                                verbosity=1,
                                title='4.4python接口测试',
                                description='接口自动化测试',
                                tester='yh')
        runner.run(dis)


if __name__ == '__main__':
    RunCase.run_test()
