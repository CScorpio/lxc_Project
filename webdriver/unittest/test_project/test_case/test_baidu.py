from selenium import webdriver
import unittest
from  time import sleep
import time
#from HTMLTestRunner import HTMLTestRunner

class Test_baidu(unittest.TestCase):
    '''百度搜索测试'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.url = "https://www.baidu.com/"
        self.driver.get(self.url)

    def test_case1(self):
        '''搜索关键字'''
        self.driver.find_element_by_id('kw').send_keys('unittest')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        title = self.driver.title
        self.assertEqual(title,"unittest_百度搜索",msg='测试失败')

    def tearDown(self):
        self.driver.close()
        print("baidu测试结束")
'''
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_baidu("test_case1"))
    #为什么不能unittest.TestSuite().addTest(Test_baidu("test_case1"))这样写？
    #因为addTest()这个方法没有返回值，只执行添加的操作 不会返回给你添加以后的suite

    #按照一定格式获取当前时间
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S")
    #定义报告的存放路径
    filename = './'+nowtime+'result.html'
    fp=open(filename,'wb')
    
    #定义测试报告存放路径
    #fp = open('./result2.html','wb')
    
    #定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='百度测试报告',
                            description='用例执行情况:')

    print("*********",type(suite))
    runner.run(suite) #执行测试用例
    fp.close() #关闭测试报告
'''