# -*- coding: UTF-8 -*-
'''
读我读我！！！！！
读我读我！！！！！
读我读我！！！！！

函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

你可以定义一个由自己想要功能的函数，以下是简单的规则：

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

下面将用一些例子来说明一些常用的函数参数定义类型

更多参数类型可参考官方文档：
FYI:http://www.runoob.com/python3/python3-function.html
'''


#此为全局变量
globalData = "this is globalData"
print('这是一个全局变量：'+globalData)

#无参函数
def methodWithNoParams():
	print("this is method with no params")

#有参函数可有多个参数 参数类型多样化
def methodWithParams(param1,param2,param3):
	print("this is method with params. param1:",param1,"param2:",param2,"param3:",param3)



#含缺省值的参数（即默认值） 需要注意的是，缺省参数必须写在非缺省参数的后面。
def methodWithDefaultParams(name,id,age,gender=True):
	print("name:%s,id:%d,age:%d,gender:%s" % (name,id,age,gender))



#函数中使用全局变量和私有变量
def methodUseParams():
	#print("globalData before update",globalData)
	#globalData = "this is private" #函数内部不可以直接修改全局变量的值，直接用“=”赋值，会被认为新建局部变量
	global globalData
	#需要使用global关键字标识，才能修改全局变量
	globalData = "update when call method"
	print("globalData after update：",globalData)

methodUseParams()
