import unittest
from calculator1 import count

class TestSub(unittest.TestCase):
    '''类的注释'''
    def setUp(self):
        print("start test")
    def testcase3(self):
        '''testcase3注释'''
        self.assertEqual(count().sub(1,5),-3,msg="判断不相等")
        print("testcase3")
    def testcase4(self):
        '''testcase4注释'''
        self.assertNotEqual(count().sub(77,1),77,msg="判断相等")
        print("testcase4")
    def tearDown(self):
        print("test end")

if __name__ =="__main__ ":
    unittest.main()
