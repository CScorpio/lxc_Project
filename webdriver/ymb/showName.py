import unittest
def showName():
	if __name__ == '__main__':
		print("i am the boss, my name is %s" % __name__)#这里进行了一个判断，如果__name__是main,也就代表是本身在调用（换句话说就是直接执行了这个文件）
	else:
		print("someone call me, caller name is %s" % __name__) #反之，不是main的，就代表是被别人调用的

def doprint():
	print("print doooooo")


if __name__ == '__main__':
	unittest.main()

#__name__ 这个东西，是每一个python文件自带的一个默认的属性。 只要写一个python,就会有他
#你可以把它理解为，调用者的名字。也就是说，谁调用了这个页面，他就是谁的名字。 其中，如果是本身调用了，就会显示__main__
#我写的这个方法就是来演示用的 你先看showName方法，
#那我现在直接运行这个文件  这里输出了第一句话，代表是本身直接执行 这个可以理解吧
#我现在是不是在showName.py这个文件里嗯 那我直接运行了showName.py 就是相当于直接执行showName.py这个文件嗯 这个裂解了吧嗯 嗯 那我们说另一种情况，就是被人调用