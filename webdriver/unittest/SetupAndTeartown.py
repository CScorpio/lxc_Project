import unittest
import time

def setUpModule():
    print("test module start >>>>>>>>>")
    time.sleep(1)

def tearDownModule():
    print("test module end  >>>>>>>>>>")
    time.sleep(1)

class SetupAndTearDown(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("set up class start ==========>")
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        print("tear down class end ==========>")
        time.sleep(1)

    def setUp(self):
        print("set up --->")
        time.sleep(1)

    def tearDown(self):
        print("tear down ---->")
        time.sleep(1)

    def test_case(self):
        print("test case 1 ")
        time.sleep(1)

    def test_case1(self):
        print("test case 2 ")
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()

