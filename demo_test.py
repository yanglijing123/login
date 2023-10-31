# -*-coding:utf-8-*-
# @Time    :2023/10/119:31
# @Author  :Ervin Chiu
# @Email   :ErvinChiu@outlook.com
# @File    :demo_test.py
# @Software:PyCharm


import unittest# 导入unittest
from unittestreport import TestRunner

class TestDemo(unittest.TestCase):
    a=4

    def setUp(self):
        print("setup")

    # @unittest.skip("莫须有")# 无条件跳过
    def test_first(self):
        self.assertEqual("导天帝","导天帝")

    #@unittest.skipIf(a>3,"莫须有")# 有条件跳过
    @unittest.skipUnless(a==5,"info")
    def test_second(self):
        self.assertEqual("导天帝", "导天帝")
    def tearDown(self):
        print("teardown")



if __name__ == '__main__':
    unittest.main()

