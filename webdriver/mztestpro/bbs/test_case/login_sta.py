# coding=utf-8
from models import myunit,function,driver
from page_obj.loginPage import login
import unittest,random,sys
from time import sleep

class loginTest(myunit.MyTest):
    '''社区登录测试'''

    #测试用户登录
    def user_login_verify(self,username='',password=''):  #由于user_login入参已经设置了默认值，所以需要将入参的默认值重新置空
        login(self.driver).user_login(username,password)

    def test_login1(self):
        '''用户名密码为空登录'''
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.user_error_hint(),'账号不能为空')
        self.assertEqual(po.pawd_error_hint(), '密码不能为空')
        function.insert_img(self.driver,"user_pawd_empty.png")


    def test_login2(self):
        '''用户名正确，密码为空登录'''
        self.user_login_verify(username='pytest')
        po = login(self.driver)
        self.assertEqual(po.pawd_error_hint(), '密码不能为空')
        function.insert_img(self.driver, "pawd_empty.png")


    def test_login3(self):
        '''用户名为空，密码正确'''
        self.user_login_verify(password='abc123456')
        po = login(self.driver)
        self.assertEqual(po.user_error_hint(), '账号不能为空')
        function.insert_img(self.driver, "user_empty.png")

    def test_login4(self):
        '''用户名与密码不匹配'''
        character = random.choice('zxcvbnmlkjhgfdsaqwertyuiop')
        username = "zhangsan" + character
        self.user_login_verify(username=username,password='123456')
        po = login(self.driver)
        self.assertEqual(po.pawd_error_hint(),"密码与账号不匹配")
        function.insert_img(self.driver,"user_pawd_error.png")

    def test_login5(self):
        self.user_login_verify(username="zhangsan",password="123456")
        sleep(2)
        po = login(self.driver)  #还有一个问题
        self.assertEqual(po.user_login_success(),'张三')
        function.insert_img(self.driver,"user_pawd_ture.png")

if __name__ == '__main__':
    unittest.main()




