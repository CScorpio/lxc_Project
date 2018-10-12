from BasePage.PAGE.Page import BasePage
from selenium.webdriver.common.by import By

class Login(BasePage):
    '''
    登录页面
    '''

    def input_username(self):
        self.find_element(By.XPATH,"//input[@id='textfield-1012-inputEl']").send_keys('root')

    def input_password(self):
        self.find_element(By.XPATH,"//input[@id='textfield-1013-inputEl']").send_keys('111111')

    def click_submit(self):
        self.find_element(By.XPATH,"//span[@id='button-1015-btnWrap']").click()
