from Page import BasePage
from selenium.webdriver.common.by import By
'''
这个是对象层，继承BasePage，该类用于定位页面元素，UI一旦有修改，只需要修改这一层的页面对象属性就行
'''
class Login126(BasePage):

    def __init__(self,driver,baseUrl,urls):
        super(Login126,self).__init__(driver,baseUrl)
        self.url = urls

    #定位器
    username_loc = (By.CLASS_NAME,"dlemail") #这里代表的是一个元组类型 用括号括起来的这种
    print(type(username_loc))
    password_loc = (By.CLASS_NAME,"dlpwd" )
    submit_loc = (By.ID,"dologin")
    text_loc = (By.CLASS_NAME,"ferrorhead")

    #输入用户名
    def input_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)#可是我不知道为什么不知道为什么要加*嗯
        #通常的写法是：find_element(By.Id,"elementId")对吧嗯
        #那么*的作用是把元组序列化 所以 usernameloc序列化以后，就是 classname dlemail

    #输入密码
    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    #点击登录按钮

    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    #返回错误信息
    def return_error_text(self):
        return  self.find_element(*self.text_loc).text
