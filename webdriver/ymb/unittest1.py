import unittest

class UnitTest1(unittest.TestCase):
 	
	def setUp(self):
		print("begin")

	def tearDown(self):
		print("finished")

	def test_function1(self):
		self.assertEqual(1,1)

	def test_function2(self):
		self.assertEqual(2,2)


if __name__ == '__main__':
	unittest.main()