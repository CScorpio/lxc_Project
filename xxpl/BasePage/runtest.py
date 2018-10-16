from BasePage.CASE.xxplcase import test_Login
import unittest

class RunTest(unittest.TestCase):
    def main(self):
        test_Login().test_login()

    if __name__ == '__main__':
        unittest.main()
