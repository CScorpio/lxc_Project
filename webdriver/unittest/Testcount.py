from count import is_prime
import unittest

class Testcount(unittest.TestCase):
    def setUp(self):
        print("start")

    def test_count(self):
        #self.assertTrue(is_prime(8),msg='is not a prime') #测试表达式的值是否为True，为False测试失败
        self.assertFalse(is_prime(7),msg='is a prime')  #测试表达式的值是否为false，为true测试失败

    def tearDown(self):
        print("end")

if __name__ == "__main__":
    unittest.main()