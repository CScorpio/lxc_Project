# -*- coding: UTF-8 -*-
# 
# OK，本篇来讲解一下关于self的东西~
# 其实讲到self,就必须先将另外一个东西 Class - 类。
# 下面将会用一个完整的新建类的示例来进行说明哦~
#


class MyFirstClass:
	'此类过来对类的声明过程进行详细的说明，可以通过__doc__方法查看到这句话。print(ClassName.__doc__)'
	address = "suzhou" #我是类变量。 可以在本类或者其他类中通过 MyFirstClass.address 访问。
	def __init__(self,name,id): #我是一个特殊的方法，当创建一个新的类，需要一些必要的参数的时候，可以使用这个方法。
		print("print when create a new class instance")
		self.name = name
		self.id = id

	def firstMethod(self,newname): #需要注意的是，所有类中的方法，都必须定义self参数，但在调用的时候，不需要传。。
		print("old name %s" % self.name)
		self.name = newname
		print("new name %s" % self.name)
		print("address",MyFirstClass.address) 

class MySecondClass:
	'此类辅助说明'
	email = "ymbmwork@foxmail.com"

	def secondMethod(self):
		print("this is secondMethod")

	def useFirstClass(self):
		firstClass = MyFirstClass("moore",99)
		print("firstclass address %s ,email %s" % (firstClass.address,MySecondClass.email))