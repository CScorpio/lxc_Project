import unittest

class SkipCase(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")
    @unittest.skip("直接跳过测试") #无条件的跳过装饰的测试，说明跳过测试的原因
    def test_skip(self):
        print("skip this case")

    @unittest.skipIf(2>1,"当条件为true时，跳过还条case") #如果条件为真时，跳过装饰的测试case
    def test_skip_if(self):
        print("if condition is true ,skip this case")

    @unittest.skipUnless(2==1,"除非条件为true时，跳过该条case") #如果条件为真的时候，不挑锅该装饰的测试case
    def test_skip_unless(self):
        print("unless condition is true,skip this case")

    @unittest.expectedFailure #测试标记失败，不管执行结果是否失败，统一标记为失败
    def test_except_failure(self):
        self.assertEqual(2,1)

if __name__ == "__main":
    unittest.main()