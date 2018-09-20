from ymb.POM.LoginFunction.Page.BaiduPage import Baidu_Page
from ymb.POM.LoginFunction.Page.WangYiPage import wangyi_page
import unittest
from selenium import webdriver
import time
class Test_Page(unittest.TestCase):
    def setUp(self):
        print("test start")
        self.driver = webdriver.Firefox()
        self.url_baidu = "https://www.baidu.com"
        self.url_wangyi = "https://www.163.com"

    #@unittest.skip("已调试好，不需要测")
    def test_BaiduLogin(self):
        '''
        1.open page
        2.login
        :return:
        '''
        baidu = Baidu_Page(self.driver,self.url_baidu)
        baidu.openPage()
        self.driver.maximize_window()
        time.sleep(2)
        baidu.clickLoginLink()
        time.sleep(2)
        baidu.switchLoginType()
        time.sleep(3)
        baidu.inputUsernameAndPassword("111","111")
        time.sleep(1)
        baidu.clickLoginBtn()
        print("baidu Login test case")

    def test_WangyiLogin(self):
        wangyi = wangyi_page(self.driver,self.url_wangyi)
        wangyi.openPage()
        self.driver.maximize_window()
        time.sleep(2)
        wangyi.click_LoginLink()
        time.sleep(2)
        wangyi.switchFrameInInputUsernameAndPassword()
        time.sleep(2)
        wangyi.input_UsernameAndPassword('222','222')
        wangyi.click_LoginBtn()
        print("wangyi Login test case")

    def tearDown(self):
        print("test end")
        self.driver.quit()


'''
    if __name__ == '__main__':
        print("run test...")
        suite = unittest.TestSuite()
        suite.addTest(Test_Page("test_WangyiLogin"))
        runner = unittest.TextTestRunner()
        runner.run(suite)
        #unittest.main()
'''