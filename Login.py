from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from Login_csv import Login_csv
import pytest
from selenium.webdriver.support.ui import Select



class Login_Page():
    Username = (By.ID, 'inputUsername')
    Password = (By.ID, 'inputPassword')
    Login_btn = (By.XPATH, '/html/body/div/form/button')
    Login_err = (By.XPATH, '/html/body/div/form/p')


class Add_Conference_Page():
    Add_btn = (By.XPATH, '/html/body/div/div[1]/div[2]/button')  # 添加按钮
    Conference_name = (By.XPATH, '//*[@id="id_name"]')  # 发布会名称
    Conference_address = (By.XPATH, '//*[@id="id_address"]')  # 发布会地址
    Conference_number = (By.XPATH, '//*[@id="id_limit"]')  # 发布会人数
    Conference_date = (By.XPATH, '//*[@id="id_start_time"]')  # 发布会日期
    commite_btn = (By.XPATH, '/html/body/div[1]/div[2]/form/div[7]/div/button')  # 提交


class Add_Guests_Page():
    Guests = (By.XPATH, '//*[@id="navbar"]/ul[1]/li[2]/a')  # 嘉宾
    Add_btn = (By.XPATH, '/html/body/div/div[1]/div[2]/button')  # 添加
    Select_name = (By.XPATH, '//*[@id="id_event"]')  # 发布会选择框
    Guests_phone = (By.XPATH, '//*[@id="id_phone"]')  # 嘉宾电话
    Guests_email = (By.XPATH, '//*[@id="id_email"]')  # 嘉宾邮箱
    Guests_name = (By.XPATH, '//*[@id="id_realname"]')
    commite_btn = (By.XPATH, '/html/body/div[1]/div[2]/form/div[7]/div/button')  # 提交


class BasePage():
    def __init__(self, driver):
        self.driver = driver


class Tset_Login_page(BasePage):  # 元素操作层

    def enter_username(self, username):
        ele = self.driver.find_element(*Login_Page.Username)
        ele.clear()
        ele.send_keys(username)

    def enter_password(self, password):
        ele = self.driver.find_element(*Login_Page.Password)
        ele.clear()
        ele.send_keys(password)

    def login_btn(self):
        ele = self.driver.find_element(*Login_Page.Login_btn)
        ele.click()

    def login_err(self):
        ele = self.driver.find_element(*Login_Page.Login_err)


class Test_Add_Conference_Page(BasePage):
    def Add_btn(self):
        ele = self.driver.find_element(*Add_Conference_Page.Add_btn)
        ele.click()

    def Enter_Conference_name(self, name):
        ele = self.driver.find_element(*Add_Conference_Page.Conference_name)
        ele.clear()
        ele.send_keys(name)

    def Enter_Conference_address(self, address):
        ele = self.driver.find_element(*Add_Conference_Page.Conference_address)
        ele.clear()
        ele.send_keys(address)

    def Enter_Conference_number(self, number):
        ele = self.driver.find_element(*Add_Conference_Page.Conference_number)
        ele.clear()
        ele.send_keys(number)

    def Enter_Conference_date(self, date):
        ele = self.driver.find_element(*Add_Conference_Page.Conference_date)
        ele.clear()
        ele.send_keys(date)

    def commite_btn(self):
        ele = self.driver.find_element(*Add_Conference_Page.commite_btn)
        ele.click()


class Test_Add_Guests_Page(BasePage):
    def Guests(self):
        ele = self.driver.find_element(*Add_Guests_Page.Guests)
        ele.click()

    def Add_btn(self):
        ele = self.driver.find_element(*Add_Guests_Page.Add_btn)
        ele.click()

    def Select_name(self):
        ele = Select(self.driver.find_element(*Add_Guests_Page.Select_name))
        ele.select_by_index(3)  # 下拉框选择项

    def Guests_phone(self, phone):
        ele = self.driver.find_element(*Add_Guests_Page.Guests_phone)
        ele.clear()
        ele.send_keys(phone)

    def Guests_email(self, email):
        ele = self.driver.find_element(*Add_Guests_Page.Guests_email)
        ele.clear()
        ele.send_keys(email)

    def Guests_name(self, gname):
        ele = self.driver.find_element(*Add_Guests_Page.Guests_name)
        ele.clear()
        ele.send_keys(gname)

    def commite_btn(self):
        ele = self.driver.find_element(*Add_Guests_Page.commite_btn)
        ele.click()


data = Login_csv(r"C:\Users\DELL\Desktop\data.csv")
print(data)


@pytest.mark.parametrize(("username", "password", "status"), data)

class TestLoginTestCase():

    def test_login_case_01(self, username, password, status):

        url = "http://150.109.156.47:8000/"
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)

        Tset_Login_page(self.driver).enter_username(username)

        Tset_Login_page(self.driver).enter_password(password)

        Tset_Login_page(self.driver).login_btn()

        if status == "0":
            Tset_Login_page(self.driver).login_err()
        else:
            print("success!!")


        Test_Add_Conference_Page(self.driver).Add_btn()

        Test_Add_Conference_Page(self.driver).Enter_Conference_name("华为")

        Test_Add_Conference_Page(self.driver).Enter_Conference_address("上海")

        Test_Add_Conference_Page(self.driver).Enter_Conference_number("100")

        Test_Add_Conference_Page(self.driver).Enter_Conference_date("2023-10-20")

        Test_Add_Conference_Page(self.driver).commite_btn()

        Test_Add_Guests_Page(self.driver).Guests()

        Test_Add_Guests_Page(self.driver).Add_btn()

        Test_Add_Guests_Page(self.driver).Select_name()

        Test_Add_Guests_Page(self.driver).Guests_phone("18103367428")

        Test_Add_Guests_Page(self.driver).Guests_email("2952243302@qq.com")

        Test_Add_Guests_Page(self.driver).Guests_name("zhangsan")

        Test_Add_Guests_Page(self.driver).commite_btn()


if __name__ == '__main__':
    pytest.main(
        ["-s", "Login.py", "--report=py_report.html", "--title=测试报告", "--tester=y", "--desc=test", "--template=2"])
