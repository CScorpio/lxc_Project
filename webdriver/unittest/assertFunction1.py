import unittest

class Test(unittest.TestCase):
    def setUp(self):
        print("start")
    def test_case(self):
        a="hello1"
        b="hello world"
        #self.assertIn(a,b,msg="a is not in b") #第一个参数是否在第二个参数中，如果不在，测试失败
        self.assertNotIn(a,b,msg="a is in b") #第一个参数是否在第二个参数中，如果在，测试失败
    def tearDown(self):
        print("end")

if __name__=='__main__':
    unittest.main()
