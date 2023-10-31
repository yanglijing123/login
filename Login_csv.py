# -*-coding:utf-8-*-
# @Time    :2023/10/2018:33
# @Author  :yanglijing
# @Email   :2952243302@qq.com
# @File    :Login_csv.py
# @Software:PyCharm
import csv

def Login_csv(file):
    mylist=[]
    with open(file,"r",encoding="utf-8")as f:
        data=csv.reader(f)
        for i in data:
            mylist.append(i)
        del mylist[0]
        return mylist

if __name__ == '__main__':
    data=Login_csv(r"C:\Users\DELL\Desktop\data.csv")
    print(data)