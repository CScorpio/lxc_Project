from HTMLTestRunner import HTMLTestRunner
from ymb.POM.LoginFunction.Test.TestPage import Test_Page
import unittest
import time

if __name__ == '__main__':
    print("run test...")
    suite = unittest.TestSuite()
    suite.addTest(Test_Page("test_BaiduLogin"))
    suite.addTest(Test_Page("test_WangyiLogin"))

    #定义文件名
    timeRemark=time.strftime("%Y-%m-%d-%H-%M-%S")
    filename='./'+timeRemark+'result.html'
    #打开文件
    fp = open(filename, 'wb')

    #报告说明 stream：翻译结果为数据流
    runner = HTMLTestRunner(stream=fp,
                            title='网页登录测试报告',
                            description='测试详情')

    runner.run(suite)
    #unittest.main()