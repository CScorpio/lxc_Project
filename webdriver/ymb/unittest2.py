import unittest

class UnitTest2(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		print("begin")

	@classmethod
	def tearDownClass(self):
		print("finished")

	def test_function3(self):
		self.assertEqual(1,1)

	def test_function4(self):
		self.assertEqual(2,2)


test_suite = unittest.TestSuite()
test_suite.addTest(UnitTest2('test_function4'))
test_suite.addTest(UnitTest2('test_function3'))

if __name__ == '__main__':
	#unittest.main()


	test_runner = unittest.TextTestRunner()
	test_runner.run(test_suite)



'''
1.什么是单元测试？ 
2.如何进行单元测试？那第二个问题就解决了吧
3.如何快捷的进行单元测试？第三个就是把每个文件里单独的测试用例抽出来，写在一整个测试的文件中。
4.如何使用单元测试框架进行单元测试？ 重点在最后一个问题上 在这之前先说一下昨天遇到的__name__的问题嗯嗯

不是说还要讲一下main呢 

test_suite = unittest.TestSuite()
	test_suite.addTest(UnitTest2('test_function4'))
	test_suite.addTest(UnitTest2('test_function3'))
	test_runner = unittest.TextTestRunner()
	test_runner.run(test_suite)
	
	这几行代码，先建了一个case集合，然后往case集合里塞case，最后执行  是这么个步骤对吧
	嗯嗯
	main() = new suite + 塞case+执行
	区别在于，main()是自动搜索当前页面中所有以test开头的方法，全部放到case集合里进行执行的。
	我昨天看书上写的是这个吧，搜索所有test开头的方法，并执行 ，是呀，但是问题是setup就不是test开头的，她怎么也执行？
	setup和teardown这两个方法，你这么理解，一个是前置函数，一个是后置函数，分别是在执行case之前和之后自动执行的，不需要手动调用。哦哦
	那main（）是不是只有这一种用法？还是我只要先记住这种用法就行 嗯 unittest.main()我一会儿去看下api说明，但你先记住这种用法就行，
	那就是，执行以后，会运行当前页面中所有test开头的case。
	
	而 建了一个case集合，然后往case集合里塞case，最后执行 这种写法，比较适合于运行指定的case，比如你写了好多个case，但你在回归的时候，并不需要去重复跑，只需要验证其中某几个，
	你就可以用这种方法 oo
	
	嗯 
	

'''
