from BasePage.PAGE.LoginPage import Login
from BasePage.PAGE.selectRole import SelectRole
from selenium import webdriver
import unittest
import time

class test_Select_Role(unittest.TestCase):
    def setUp(self):
        self.url = 'http://192.168.1.101:7400/faext_s460/index.html'
        driver = webdriver.Firefox()

        self.sr = SelectRole(driver, self.url) #因为这块重新new的实例，我不知道是不是因为这个原因，导致他还在前一个页面上
        print('test_Select_Role测试开始')

    def tearDown(self):
        print('test_Select_Role测试结束')


    def test_select_role(self,driver = None):
        if(driver!=None):
            sr = SelectRole(driver, self.url)
        else:
            sr = SelectRole

        sr = SelectRole(driver,self.url)
        sr.select_functionrole()
        sr.select_datarole()
        sr.click_confirm()


