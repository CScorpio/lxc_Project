from test_case.test_baidu import Test_baidu
from test_case.test_youdao import Test_Youdao
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

#if __name__ == '__main__':
#    unittest.main()
'''
suite = unittest.TestSuite()
suite.addTest(Test_baidu('test_case1'))
suite.addTest(Test_Youdao('test_case2'))
'''

suite = unittest.defaultTestLoader.discover(start_dir='./test_case',pattern='test*.py')

if __name__ == '__main__':
    #定义报告的存放路径
    test_dir = './' #路径
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = test_dir +nowtime+'result.html'

    #通过open方法以二进制写模式打开存放路径下的filename文件
    fp = open(filename,'wb')

    #调用HTMLTestRunner()类，stream指定测试报告的文件，title定义报告的标题，description 用于定义测试报告的副标题
    runner= HTMLTestRunner(stream=fp,
                   title="测试报告",
                   description="用例执行情况")



    #unittest.TextTestRunner().run(suite)
    runner.run(suite)
    fp.close() #注意：要关闭测试报告文件
