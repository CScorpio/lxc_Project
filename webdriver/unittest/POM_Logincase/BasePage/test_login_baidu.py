from LoginBaidu import Login_baidu
from selenium import webdriver
import unittest
import time

class test_login_baidu(unittest.TestCase):

    url = '/'
    def setUp(self):
        print("baidu test start")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = 'https://www.baidu.com'
        self.username = 'root'
        self.password = '111111'

    def test_login_baidu_case(self):
        login_baidu = Login_baidu(self.driver,self.base_url,self.url)
        login_baidu.open()
        login_baidu.click_login_button()
        time.sleep(2)
        login_baidu.click_un_pw_baidu_loc()
        login_baidu.input_username(self.username)
        login_baidu.input_password(self.password)
        login_baidu.click_submit()
        time.sleep(1)
        text = login_baidu.alert_text()

        print(text)
        try:
            self.assertEqual(text,'请您输入验证码',msg='提示信息错误')
        except AssertionError as msg:
            print(msg)

    def tearDown(self):
        print("baidu test end")
        #self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

