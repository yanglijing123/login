# -*-coding:utf-8-*-
# @Time    :2023/10/3016:58
# @Author  :yanglijing
# @Email   :2952243302@qq.com
# @File    :Login_run.py
# @Software:PyCharm
import unittest
import HTMLTestRunnerNew


suite=unittest.defaultTestLoader.discover("D:\python\python project\python Project1\wk1",pattern="Login.py") #用例文件的路径

with open("reports.html", "wb+")as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(file, 2, title="testlogin", tester="ylj", description="unittest")
    runner.run(suite)