from BasePage.PAGE.LoginPage import Login
from BasePage.PAGE.selectRole import SelectRole
from selenium import webdriver
import unittest
import time
import requests

class test_Login(unittest.TestCase):

    def setUp(self):
        self.url = 'http://192.168.1.101:7400/faext_s460/index.html'
        self.driver = webdriver.Firefox()
        self.loginpye = Login(self.driver, self.url)
        print('test_Login测试开始')

    def tearDown(self):
        print('test_Login测试结束')


    def test_login(self):
        self.loginpye.open(self.url)
        time.sleep(2)
        self.loginpye.input_username()
        self.loginpye.input_password()
        time.sleep(1)
        self.loginpye.click_submit()

        time.sleep(3)

        #select_page_html = self.driver.page_source
        #print(select_page_html)

        #return self.driver

    def test_select_role(self, driver=None):
        sr = SelectRole(driver, self.url)
        sr.select_functionrole()
        sr.select_datarole()
        sr.click_confirm()


