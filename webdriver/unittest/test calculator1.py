import unittest
from calculator import count

class test_add(unittest.TestCase):
    def setUp(self):
        print("test start")
    def test_case1(self):
        self.assertEqual(count().add(1,2),3,msg='test fail1')
    def test_case2(self):
        self.assertNotEqual(count().add(77,1),78,msg='test fail2')
    def tearDown(self):
        print("test end")

class test_sub(unittest.TestCase):
    def setUp(self):
        print("test start")
    def test_case3(self):
        self.assertEqual(count().sub(1,10),-8,msg='test fail3')
    def test_case4(self):
        self.assertNotEqual(count().sub(8,2),5,msg='test fail4')
    def tearDown(self):
        print("test end")

if __name__ == "__main__":
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(test_add("test_case1"))
    suite.addTest(test_add("test_case2"))
    suite.addTest(test_sub("test_case3"))
    suite.addTest(test_sub("test_case4"))

    #运行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

