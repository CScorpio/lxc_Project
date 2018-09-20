from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Page(object):
    '''
    基础类，用于页面对象类的继承
    '''
    login_url = 'https://www.126.com'
    def __init__(self,selenium_driver,base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        print("assert",self.driver.current_url)
        print(self.driver.current_url == (self.base_url+self.url))
        return self.driver.current_url == (self.base_url+self.url)

    def _open(self,url):
        print("_open url:",self.url)
        print("_open base url:",self.base_url)
        url = self.base_url+self.url
        print("_open url after combo:",url)

        self.driver.get(url)
        assert self.on_page(), 'did not land on %s' %url

    def open(self):
        print("open url:",self.url)
        self._open(self.url)

    def find_element(self,*loc):
        #self.driver.switch_to_frame("x-URS-iframe") 如果将switch_to_frame写在此处，那么在调用type_username
        sleep(1)
        return self.driver.find_element(*loc)

class LoginPage(Page):
    '''
    126邮箱登录页面模型
    '''
    url = '/'

    #定位器
    username_loc = (By.CLASS_NAME,"j-inputtext.dlemail")
    password_loc =(By.CLASS_NAME,"j-inputtext.dlpwd" )
    submit_loc = (By.ID,"dologin")

    #Action
    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()


def test_user_login(driver,username,password):
        '''
        测试获取的用户名密码是否可以登录
        '''
        login_page = LoginPage(driver)
        login_page.open()
        sleep(1)
        driver.switch_to_frame('x-URS-iframe')
        login_page.type_username(username)
        login_page.type_password(password)
        login_page.submit()



def main():
    try:
        driver = webdriver.Firefox()
        username = 'username'
        password = '123456'
        test_user_login(driver,username,password)
        sleep(3)
        text = driver.find_element_by_xpath("//div[@class='ferrorhead']").text
        try:
            assert (text == 'username@126.com'),"需要输入验证码"
        except AssertionError as msg:
            print(msg)
    finally:
        #关闭浏览器窗口
        #driver.close()
        print("finished")

if __name__ == '__main__':
    main()
