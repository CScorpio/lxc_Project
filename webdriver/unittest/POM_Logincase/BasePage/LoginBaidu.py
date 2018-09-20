from Page import BasePage
from selenium.webdriver.common.by import By

class Login_baidu(BasePage):

    def __init__(self,driver,baseUrl,urls):
        super(Login_baidu,self).__init__(driver,baseUrl)
        self.url = urls

    #定位器
    username_baidu_loc = (By.ID,'TANGRAM__PSP_10__userName')
    password_baidu_loc = (By.ID,'TANGRAM__PSP_10__password')
    submit_baidu_loc = (By.ID,'TANGRAM__PSP_10__submit')
    login_button = (By.LINK_TEXT,'登录')
    un_pw_baidu_loc = (By.XPATH,"//p[@title='用户名登录']")
    alert_text_loc = (By.ID,'TANGRAM__PSP_10__error') #TANGRAM__PSP_10__error

    #点击登录按钮
    def click_login_button(self):
        self.find_element(*self.login_button).click()

    #点击用户名密码登录
    def click_un_pw_baidu_loc(self):
        self.find_element(*self.un_pw_baidu_loc).click()

    #输入用户名
    def input_username(self,username):
        self.find_element(*self.username_baidu_loc).send_keys(username)

    #输入密码
    def input_password(self,password):
        self.find_element(*self.password_baidu_loc).send_keys(password)

    #点击提交按钮
    def click_submit(self):
        self.find_element(*self.submit_baidu_loc).click()

    #提示信息
    def alert_text(self):
        textEle = self.find_element(*self.alert_text_loc)
        print("===========")
        print("alert text is displayed :",textEle.is_displayed())
        text_result=textEle.text
        print("alert text is :",text_result)
        return text_result
