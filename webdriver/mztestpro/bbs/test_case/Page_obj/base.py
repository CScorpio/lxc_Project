# coding=utf-8
'''
创建页面基础类
'''


class Page(object):
    '''
    页面基础类，用于所有页面的继承
    '''
    bbs_url = 'http://bbs.meizu.con'

    def __init__(self,selenium_driver,base_url = bbs_url,parent = None):  #初始化参数
        self.driver = selenium_driver
        self.base_url = base_url
        self.timeout = 30
        self.parent = parent

    def _open(self,url):              #受保护的函数
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(),'did not land on %s' %url

    def find_element(self,*loc):
        self.driver.find_element(*loc)

    def find_elements(self,*loc):
        self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self,src):
        return self.driver.execute_script(src)
