import unittest
from calculator import count

class myTest(unittest.TestCase):
    def setUp(self):
        print("test start")
    def tearDown(self):
        print("test end")

class test_add(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(count().add(1,2),3,msg='test fail1')
    def test_case2(self):
        self.assertNotEqual(count().add(77,1),79,msg='test fail2')


class test_sub(unittest.TestCase):
    def test_case3(self):
        self.assertEqual(count().sub(1,10),-9,msg='test fail3')
    def test_case4(self):
        self.assertNotEqual(count().sub(8,2),5,msg='test fail4')


if __name__ == "__main__":
    unittest.main()

