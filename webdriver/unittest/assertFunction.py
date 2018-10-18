import unittest

class Test(unittest.TestCase):

    def setUp(self):
        number=input("Enter a number:")
        self.number = int(number)

    def testCase(self):
        self.assertEqual(self.number, 10, "输入的数字不是10")
        '''
        try :
            self.assertEqual(self.number,10,"输入的数字不是10")
        except BaseException as msg:
            print("++++++++++++++++++")
            print(msg)
            print("bababababbababababababababababab~wuwuwuwuwuwuwwu~yei") 
        '''


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()