from calculator import count
import unittest

'''
class test_count():
    a = float(input('输入任意一个数字a：'))
    b = float(input('输入任意一个数字b：'))
    count.add(a,b)
'''
'''
class TestCount:
    def test_add(self):
        try:
            j = count()
            add = j.add(2,3)
            assert(add==7),'Integer addition result error!'
        except AssertionError as msg:
            print(msg)
        else:
            print("Test pass")

TestCount().test_add()
'''

'''
class TestCount:
    def test_add(self):

        j = count()
        add = j.add(2, 3)
        if add==5:
            print("Test pass")
        else:
            print("Integer addition result error!")

TestCount().test_add()
'''

'''
class TestCount(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j=count()
        self.assertEqual(j.add(2,5),7)

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    unittest.main()
'''


class TestCount1(unittest.TestCase):

    def setUp(self):
        print("test start")
    def testadd1(self):
        self.assertEqual(count().add(1,5),6,msg='不相等') #第一个参数和第二个参数是否相等，不相等则测试失败
    def testadd2(self):
        self.assertNotEqual(count().add(777777,1),777778) #第一个参数和第二个参数是否不相等，相等测试失败
    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    #构造函数集
    suite = unittest.TestSuite()
    suite.addTest(TestCount1('testadd2'))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

print("*******")
TestCount1().testadd1()
print("*******")

