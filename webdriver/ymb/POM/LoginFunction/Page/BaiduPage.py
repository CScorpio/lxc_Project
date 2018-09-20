from ymb.POM.LoginFunction.Page.BasePage import  Base_Page
from selenium.webdriver.common.by import By

class Baidu_Page(Base_Page):
    '''
    1.Login
    1.1 driver.get("http://www.baidu.com")
    1.2 find login link, click it
    1.3 click login by username&password link
    1.4 find username&password input element ,and input value
    1.5 click loginBtn
    '''

    def clickLoginLink(self):
        loginLink = self.findElement(By.LINK_TEXT,"登录")
        self.click(loginLink)

    def switchLoginType(self):
        loginTypeLink = self.findElement(By.ID,"TANGRAM__PSP_10__footerULoginBtn")
        self.click(loginTypeLink)


    def inputUsernameAndPassword(self,username,password):
        usernameElement = self.findElement(By.ID,"TANGRAM__PSP_10__userName")
        passwordElement = self.findElement(By.ID,"TANGRAM__PSP_10__password")
        self.sendKeys(usernameElement,username)
        self.sendKeys(passwordElement,password)

    def clickLoginBtn(self):
        loginBtn = self.findElement(By.ID,"TANGRAM__PSP_10__submit")
        self.click(loginBtn)




