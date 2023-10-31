# -*-coding:utf-8-*-
# @Time    :2023/10/2310:17
# @Author  :yanglijing
# @Email   :2952243302@qq.com
# @File    :email.py
# @Software:PyCharm


# -*-coding:utf-8-*-
# @Time    :2023/10/119:44
# @Author  :Ervin Chiu
# @Email   :ErvinChiu@outlook.com
# @File    :test_demo01.py
# @Software:PyCharm
# coding: utf-8
import HTMLTestRunnerNew
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
import pathlib
import os
import unittest
import HTMLTestRunner
from demo_test import TestDemo


def send_mail(username, passwd, recv, title, content, mail_host='smtp.qq.com', port=25, file=None):
    '''
    发送邮件函数，默认使用qqsmtp
    :param username: 邮箱账号 xx@qq.com
    :param passwd: 邮箱密码
    :param recv: 邮箱接收人地址，多个账号以逗号隔开
    :param title: 邮件标题
    :param content: 邮件内容
    :param mail_host: 邮箱服务器
    :param port: 端口号
    :return:
    '''
    if file:
        msg = MIMEMultipart()
        # 构建正文
        part_text = MIMEText(content)
        msg.attach(part_text)  # 把正文加到邮件体里面去

        # 构建邮件附件
        part_attach1 = MIMEApplication(open(file, 'rb').read())  # 打开附件
        part_attach1.add_header('Content-Disposition', 'attachment', filename=pathlib.Path(file).name)  # 为附件命名
        msg.attach(part_attach1)  # 添加附件
    else:
        msg = MIMEText(content)  # 邮件内容
    msg['Subject'] = title  # 邮件主题
    msg['From'] = username  # 发送者账号
    msg['To'] = recv  # 接收者账号列表
    smtp = smtplib.SMTP(mail_host, port=port)
    smtp.login(username, passwd)  # 登录
    smtp.sendmail(username, recv, msg.as_string())
    smtp.quit()


send_address = "2952243302@qq.com"
send_password = "nadsvhosilnddebf"
receive_address = "3588290647@qq.com"
title = "聚师网UI自动化测试报告"
content = "Hi，你好！此邮件为自动发送，不必回复~详情请查看附件，如有疑问可联系测试组~"
attachfilepath = r"D:\python\python project\python Project1\wk\reports"
lists = os.listdir(attachfilepath)
lists.sort(key=lambda fn: os.path.getmtime(attachfilepath + "\\" + fn))
file = os.path.join(attachfilepath, lists[-1])
send_mail(send_address, send_password, receive_address, title, content, file=file)
print('Email Send Success!!')

suite = unittest.TestSuite()

suite.addTest(TestDemo("test_first"))
suite.addTest(TestDemo("test_second"))

with open("test.html", "wb+") as file:
    # runner = unittest.TextTestRunner(file,"test",2)
    # runner.run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(file, 2, title="testcase", description="unittest")
    runner.run(suite)
    send_mail(send_address,send_password,receive_address,title,content)