from selenium import webdriver

'''
基础类basePage,封装所有页面都公用的方法【页面操作的基本方法】
定义一个open函数，重定义findelement，sendkeys等方法
在初始化方法中定义驱动driver，url

'''
class BasePage(object):
    '''
    basePage封装所有页面都公用的方法，例如driver、url、findelement等
    '''
    #初始化driver，url
    #实例化BasePage时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参
    #__init__方法不能有返回值，只能返回none
    #
    def __init__(self,driver,base_url):
        self.driver=driver
        self.base_url=base_url
        self.timeout=30

    #通过路径来断言判断访问的页面是否正确，返回比较结果（true或者false）
    def on_page(self):
        print(self.driver.current_url==self.url)
        return self.driver.current_url == self.url

    #打开页面，并且校验页面链接是否加载正确
    #以单下划线开头的方法，为受保护的方法，只有当前类和子类的对象可以使用
    #并且以单下划线开头的方法，使用from module import *时不会被获取，但是使用import module可以获取
    def _open(self,url):
        print(url)
        print(self.base_url)
        url = self.base_url+url #这里的url是在_open方法内部声明的一个变量，他不是slef.url 所以 改变了这个url的值，并不是改变了self。url的值
        #这一步执行完以后 他们的值分别是： slef.url = "/" url = "https://www.126.com/"
        #使用get打开访问链接
        self.driver.get(url) # 这里为什么传self.url不行，由于上面并没有改变self.url的值，所以这个地方还是要传url，这个url才是真正拼接完的完整url

        #使用assert进行校验，判断当前打开的链接driver.current_url和要访问的链接url是否一致，此时调用on_page()方法
        assert not self.on_page(),'did not land on %s' %url



    #定义open方法，调用_open()方法打开链接
    def open(self):
        self._open(self.url)

    #重写元素定位方法
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    #感觉还可以吧send_keys抽出来
    def send_keys(self,text):
        if not isinstance(text, list):
            text = keys_to_typing(text)
        for letter in text:
            self.key_down(letter, element)
            self.key_up(letter, element)
        return self

