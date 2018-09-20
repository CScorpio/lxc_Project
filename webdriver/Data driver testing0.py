from selenium import  webdriver
from webdriver.publicloginout import Loginout


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://192.168.1.101:7100/ifsp/login.html")

class LoginTest:

    def adminLogin(self):
        un='root'
        pw='111111'
        Loginout.Login(driver,un,pw)


    def fqyLogin(self):
        un='fqy'
        pw='111111'
        Loginout.Login(driver,un,pw)

LoginTest().adminLogin()
driver.refresh()
LoginTest().fqyLogin()



'''用户名密码入参'''

'''
#调用登录方法
driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://192.168.1.101:7100/ifsp/login.html")

#Loginout.Login(driver) #调用登录方法
'''

'''
#用户名密码入参调用
driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://192.168.1.101:7100/ifsp/login.html")

Loginout.Login(driver,'root','111111') #root用户登录
driver.refresh()
time.sleep(2)
Loginout.Login(driver,'fqy','111111') #fqy用户登录
'''

'''
class LoginTest():
    def _init_(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://192.168.1.101:7100/ifsp/login.html")

    def adminLogin(self):
        un='root'
        pw='111111'
        Loginout.Login(self.driver,un,pw)


    def fqyLogin(self):
        self.driver.refresh()
        un='fqy'
        pw='111111'
        Loginout.Login(self.driver,un,pw)

LoginTest.adminLogin()
LoginTest.fqyLogin()

'''
