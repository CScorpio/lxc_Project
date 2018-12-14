from HTMLTestRunner import HTMLTestRunner
from  selftest import LoginBaidu
import unittest
import time

suite = unittest.TestSuite()
suite.addTest(LoginBaidu('test_all_null'))
suite.addTest(LoginBaidu('test_password_is_null'))
suite.addTest(LoginBaidu('test_password_is_wrong'))

#if __name__ == '__main__':
#定位报告生成的文件
test_dir='./'
nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
file_name = test_dir + nowtime + 'baiduLoginResult.html'

#打开这个文件
fp = open(file_name,'wb')

#创建一个runner
runner = HTMLTestRunner(stream=fp,
                   title='百度登录测试报告',
                   description='用例执行情况')

#runner=unittest.TextTestRunner()
runner.run(suite)

#关闭这个文件
fp.close()

'''
第一种方式：直接调用main方法
if __name__ == '__main__'：      
    unittest.main()     

第二种方式：构造测试集
suite = unittest.TestSuite()
suite.addTest(LoginBaidu('test_all_null'))
suite.addTest(LoginBaidu('test_password_is_null'))
suite.addTest(LoginBaidu('test_password_is_wrong'))
if __name__ == '__main__'：
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
第三种方式：使用discover()方法，找到要测试的文件

test_dir='./'
discover_case = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ = '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
    
第四种方式：生成测试报告


test_dir='./'
 

nowtime = time.strftime('Y_%m_%d_%H_%M_%S')
file_name = test_dir + nowtime + 'result.html'

fp = open(file_name)   #报告的存放路径

runner = HTMLTestRunner(stream=fp,             #定义测试报告
                        title='test report',
                        description='case detail')
discover_case = unittest.defaultTestLoader.doscover(test_dir,pattern='test*.py') #找测试用例，也可以用suite
runner.run(discover_case)  #运行测试用例

fp.close() #关闭报告文件 

问题1：if __name__=='__main__':的使用说明，什么情况下用这句话，用不用的区别在哪里？
    该判断条件在测试方法和功能方法分开的情况下，这个判断语句使用与否都可以，但是当测试方法和功能方法写在一起的情况下，
问题2：每一种方式有什么优缺点
                        
'''






