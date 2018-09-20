from Page import BasePage
from selenium.webdriver.common.by import By

class LoginPye(BasePage):

    def __init__(self,driver,baseUrl,urls):
        super(LoginPye,self).__init__(driver,baseUrl)
        self.url = urls


    #定位器
    username_pye_loc = (By.ID,'textfield-1012-inputEl')
    password_pye_loc = (By.ID,'textfield-1013-inputEl')
    submit_pye_loc = (By.ID,'button-1015-btnWrap')
    test_loc = (By.CLASS_NAME,'x-header-text.x-window-header-text.x-window-header-text-default')

    #输入用户名
    def input_username(self,username):
        self.find_element(*self.username_pye_loc).send_keys(username)

    #输入密码
    def input_password(self,password):
        self.find_element(*self.password_pye_loc).send_keys(password)

    #点击提交按钮
    def click_submit(self):
        self.find_element(*self.submit_pye_loc).click()

    #获取选择觉得的文本
    def get_text(self):
        return self.find_element(*self.test_loc).text