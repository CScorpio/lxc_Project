# coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    '''
    用户登录页面
    '''
    url = '/'

    #Action，定位器
    bbs_login_user_loc = (By.XPATH,"//div[@id=zuCust']/div/img")
    bbs_login_button_loc = (By.ID,"mzLogin")

    def bbs_login(self):
        self.find_element(*self.bbs_login_user_loc).click()
        sleep(1)
        self.find_element(*self.bbs_login_button_loc).click()

    login_username_loc = (By.ID,"account")
    login_password_loc = (By.ID,"password")
    login_button_loc = (By.ID,"login")

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

    #登录按钮
    def login_butthon(self):
        self.find_element(*self.login_button_loc).click()

    #定义统一登录入口
    def user_login(self,username = 'username',password = '111111'): #此时为username和password入参设置默认值是为了方便其他用例在调用时
        """获取用户名密码登录"""                                       #不需要再传递登录用户的信息，因为大多数的执行都用这个账号
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_butthon()
        sleep(1)

    user_error_hint_loc = (By.XPATH,"//span[@for = 'account']")
    pawd_errow_hint_loc = (By.XPATH,"//span[@for = 'password']")
    user_login_success_loc = (By.ID,"mzCustName")

    #用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    #密码错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.pawd_errow_hint_loc).text

    #登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text





