from selenium import webdriver
import unittest
from time import sleep

class Test_Youdao(unittest.TestCase):
    '''有道搜索测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://www.youdao.com/")

    def test_case2(self):
        '''搜索关键字'''
        driver = self.driver
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys("你好")
        driver.find_element_by_xpath("//*[@id='form']/button").click()
        title = driver.title
        self.assertEqual(title,'【你好】英语怎么说_在线翻译_有道词典',msg='测试失败')

    def tearDown(self):
        print("youdao测试结束")
        self.driver.quit()