from Login126 import Login126
from Page import BasePage
from selenium import webdriver
import unittest
import time

class test_login_126(unittest.TestCase):
    url = '/'
    def setUp(self):
        print("test start")
        self.base_url = 'https://www.126.com'
        self.driver = webdriver.Firefox()
        self.username = 'root'
        self.password = '123456'



    def test_user_login_126(self):
        login126 = Login126(self.driver,self.base_url,self.url)   #子类继承父类以后，如果没有明确声明自己的初始化方法的话，会默认执行父类的初始化方法
        login126.open()#子类继承了父类的方法，所以不需要用父类来打开了 直接调用子类里面的就好啦
        time.sleep(2)
        self.driver.switch_to.frame('x-URS-iframe')
        login126.input_username(self.username)
        login126.input_password(self.password)
        login126.click_submit()
        time.sleep(2)
        '''
        error_text_loc=self.driver.find_element_by_class_name('ferrorhead').text
        try:
            self.assertNotEqual(error_text_loc,"帐号或密码错误",msg='账号或者密码错误')
        except AssertionError as msg:
            print(msg)
        '''
        error_text = login126.return_error_text()
        try:
            self.assertEqual(error_text,"帐号或密码错误",msg='提示信息有误')
        except AssertionError as msg:
            print(msg)


    def tearDown(self):
        print("test end")
        self.driver.quit()


    def main(self):
        self.test_user_login_126()


    if __name__ == '__main__':
        unittest.main()

