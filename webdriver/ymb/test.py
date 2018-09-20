import unittest

class Mathmethod(unittest.TestCase):
    def add(self):
        print("add")

    def sub(self):
        print("sub")


    def setUp(self):
        print("set up")

    def tearDown(self):
        print("tear down")

    def test_add(self):
        print("test add")

    def test_sub(self):
        print("test sub")


if __name__ == '__main__':
    unittest.main()