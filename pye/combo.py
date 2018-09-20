# -*- coding: UTF-8 -*-
import function
from classintro import MyFirstClass
from classintro import MySecondClass

#function 使用说明
print("============methodWithNoParams============")
function.methodWithNoParams()
print(" ")

print("============methodWithParams============")
function.methodWithParams("abcedfg",123454,True)
print(" ")

print("============methodWithDefaultParams============")
function.methodWithDefaultParams("moore",1002,18)
function.methodWithDefaultParams("baby",1111,16,False)
print(" ")

print("============methodUseParams============")
function.methodUseParams()
print(" ")


#class使用说明
fc = MyFirstClass("newclass",1)
fc.firstMethod("changename")

sc = MySecondClass()
sc.secondMethod()
sc.useFirstClass()