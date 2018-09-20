import unittest
from  calculator1 import count

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("start test")
    def testcase1(self):
        self.assertEqual(count().add(1,2),3,msg='判断不相等')
        print("testcase1")
    def testcase2(self):
        self.assertNotEqual(count().add(77,1),79,msg="相等")
        print("testcase2")
    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    unittest.main()

