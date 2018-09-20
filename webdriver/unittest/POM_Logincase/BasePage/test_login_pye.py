
from LoginPye import LoginPye
import unittest
from selenium import webdriver
import time

class test_login_pye(unittest.TestCase):
    url='/ifsp/login.html'
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://192.168.1.101:7100/ifsp/login.html'
        self.username = 'root'
        self.password = '111111'
        print("pye test start")

    def test_login_pye_case(self):
        loginpye = LoginPye(self.driver,self.base_url,self.url)
        loginpye.open()
        loginpye.input_username(self.username)
        loginpye.input_password(self.password)
        time.sleep(2)
        loginpye.click_submit()
        time.sleep(2)
        text = loginpye.get_text()
        try:
            self.assertEqual(text,'角色选择',msg="页面没有跳转成功")
        except AssertionError as msg:
            print(msg)


    def tearDown(self):
        print("test end")
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()