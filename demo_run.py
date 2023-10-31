# -*-coding:utf-8-*-
# @Time    :2023/10/2311:44
# @Author  :yanglijing
# @Email   :2952243302@qq.com
# @File    :demo_run.py
# @Software:PyCharm
import unittest
from  unittestreport import TestRunner
from demo_test import *


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDemo('test_first'))
    runner = TestRunner(suite)
    runner.run()
    runner.send_email(host="smtp.qq.com",
                      port=465,
                      user="2952243302@qq.com",
                      password="nadsvhosilnddebf",
                      to_addrs="3588290647@qq.com")