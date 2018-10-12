from BasePage.CASE.LoginCase import test_Login
from BasePage.CASE.SelectRoleCase import test_Select_Role
import unittest

class RunTest(unittest.TestCase):

    def main(self):
        lastDriver = test_Login.test_login()
        #我想尝试，把之前的driver返回出来，然后传到下一个类里面 看看行不行
        test_Select_Role.test_select_role(lastDriver)
    if __name__ == '__main__':
        unittest.main()
