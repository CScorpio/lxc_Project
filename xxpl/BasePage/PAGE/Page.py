from selenium import webdriver

class BasePage(object):
    '''
    封装所有页面都公用的方法，例如driver、url、findelement等
    '''
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def open(self,url):
        return self.driver.get(url)

    def find_element(self,type,value):
        return self.driver.find_element(type,value)


