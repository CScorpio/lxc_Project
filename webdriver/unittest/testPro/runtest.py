import testadd
import testsub
import calculator1
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

#构建测试集
suite = unittest.TestSuite()
suite.addTest(testadd.TestAdd("testcase1"))
suite.addTest(testadd.TestAdd("testcase2"))
suite.addTest(testsub.TestSub("testcase3"))
suite.addTest(testsub.TestSub("testcase4"))

#执行测试
unittest.TextTestRunner().run(suite)
'''
if __name__  == "__main__":
    unittest.TextTestRunner().run(suite)
'''



'''
#使用unittest中的defaultTestLoader类下的discover()方法来加载测试用例
#定义测试用例的目录为当前目录
test_dir='./' #定义测试用例的目录为当前目录

discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

discover()方法说明：discover(self, start_dir, pattern='test*.py', top_level_dir=None)
start_dir:要测试的模块名称或者测试用例的目录
pattern='test*.py' 表示用例文件名的匹配原则。此处匹配文件名以"test"开头的.py类型的文件，*表示任意多个目录
top_level_dir：测试模块的顶层目录，如果没有顶层目录，默认为None  



if __name__ == '__main__':
    unittest.TextTestRunner().run(discover)
'''


'''
if __name__ == '__main__':

    suite = unittest.defaultTestLoader.discover(start_dir='./',pattern='test*.py')


    test_dir = './'
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S")
    file_name = test_dir+nowtime+'calculatorResult.html'

    fp = open(file_name,'wb')

    runner = HTMLTestRunner(stream=fp,
                            title="calculator测试用例",
                            description="测试结果")
    runner.run(suite)
    fp.close()

'''