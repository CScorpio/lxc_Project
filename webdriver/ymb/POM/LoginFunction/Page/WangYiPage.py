from ymb.POM.LoginFunction.Page.BasePage import Base_Page
from selenium.webdriver.common.by import By

class wangyi_page(Base_Page):
    '''
    1.Login
    1.0 open page
    1.1 find Login link and click it
    1.2 input username and password
    1.3 click login btn
    '''
    def click_LoginLink(self):
        Login_link=self.findElement(By.LINK_TEXT,"登录")
        self.click(Login_link)

    def switchFrameInInputUsernameAndPassword(self):
        iframe= self.driver.find_element_by_xpath("//*[@id='js_N_login_wrap']/iframe")
        self.switchframe(iframe)
        print(iframe)

    def input_UsernameAndPassword(self,username,password):
        usernameElement=self.findElement(By.XPATH,"//input[@data-placeholder='网易邮箱/常用邮箱']")
        passwordElement=self.findElement(By.XPATH,"//input[@data-placeholder='请输入密码']")
        self.sendKeys(usernameElement,username)
        self.sendKeys(passwordElement,password)

    def click_LoginBtn(self):
        Login_btn=self.findElement(By.ID,'dologin')
        self.click(Login_btn)

