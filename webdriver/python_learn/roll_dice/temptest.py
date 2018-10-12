import matplotlib.pyplot as plt
import numpy as np

print(np.arange(2,13))
print(np.arange(2,13)+0.5) #哈哈 看出效果来了
print(np.arange(2,13)-0.5) #根据我们写的例子,arange()+n 会改变数组里每个元素的值 改变的大小就是后面加减的值嗯嗯，我知道了，这个
#数组类型的其实在python中没有的，但是这个numPy是有的这个是一个包不对，模块？就那个意思# 这是模块嗯嗯
print(np.arange(2,13)*2)
print(np.arange(2,13)/2)  #这个加减乘除都行 点时什么鬼代表小数 1.  = 1.0 好吧
#下一个方法

print("############################")

plt.hist([1,2,3,4,5],bins=range(1,7),edgecolor = 'black',linewidth = 1,density=1) #这是画图


locs,labels = plt.xticks(np.arange(1,6)+0.5,['1','2','3','4','5'])

plt.show()

#print(locs)
#print(labels)
#把返回的这个结果 画个柱状图出来