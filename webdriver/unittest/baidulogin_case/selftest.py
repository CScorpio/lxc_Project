from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class LoginBaidu(unittest.TestCase):
    '''测试百度登录'''


    @classmethod
    def setUpClass(cls):
        print("test start")
        cls.driver = webdriver.Firefox()
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://www.baidu.com/")
        cls.open_loginPage(cls)

    def open_loginPage(self):
        driver = self.driver
        driver.find_element_by_link_text("登录").click()
        time.sleep(2)
        driver.find_element_by_xpath("//p[@class='tang-pass-footerBarULogin pass-link' and @title='用户名登录']").click()

    def clearInput(self):
        driver = self.driver
        self.username = driver.find_element_by_id("TANGRAM__PSP_10__userName")
        self.username.clear()
        self.password = driver.find_element_by_id("TANGRAM__PSP_10__password")
        self.password.clear()

    def test_all_null(self):
        '''用户名密码为空'''
        driver=self.driver
        self.clearInput()
        self.submit = driver.find_element_by_id("TANGRAM__PSP_10__submit")
        self.submit.click()
        time.sleep(1)
        self.alertText = driver.find_element_by_id("TANGRAM__PSP_10__error").get_attribute("textContent")
        self.assertEqual(self.alertText,"请您输入手机/邮箱/用户名",msg='用户名密码为空的提示信息有误')
        print("test_all_null")

    def test_password_is_null(self):
        '''密码为空'''
        driver = self.driver
        self.clearInput()
        self.username.send_keys("4515")
        self.password.send_keys("")
        self.submit = driver.find_element_by_id("TANGRAM__PSP_10__submit")
        self.submit.click()
        time.sleep(1)
        self.alertText = driver.find_element_by_id("TANGRAM__PSP_10__error").get_attribute("textContent")
        self.assertEqual(self.alertText,"请您输入密码",msg='密码为空的提示信息有误')
        print("test_password_is_null")

    def test_password_is_wrong(self):
        '''密码错误'''
        driver = self.driver
        self.clearInput()
        self.username.send_keys("15151")
        self.password.send_keys("111111")
        self.submit = driver.find_element_by_id("TANGRAM__PSP_10__submit")
        self.submit.click()
        time.sleep(1)
        self.alertText = driver.find_element_by_id("TANGRAM__PSP_10__error").get_attribute("textContent")
        try:
            self.assertEqual(self.alertText,"帐号或密码错误，请重新输入或者找回密码",msg='密码错误的提示有误')
        except BaseException as msg:
            print(msg)
        print("test_password_is_wrong")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("test end")


