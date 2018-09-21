'''
v4.0功能：科学计算
'''

import random
import matplotlib.pyplot as plt
import numpy as np

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei'] #由于matplotlib默认支持输出英文，所以需要修改参数，输入字体为黑体
plt.rcParams['axes.unicode_minus'] = False

def main():
    '''
    投掷筛子
    '''
    #投掷筛子的次数
    roll_times = 10000

    roll1_result = np.random.randint(1,7,size=roll_times) #np.random.randint(a,b,size)创建[a,b)间形状为size的数组
    roll2_result = np.random.randint(1,7,size=roll_times)
    rollresult = roll1_result +roll2_result #以数组为对象进行基本运算，即向量化操作，两个数组同位置处的数据进行相加操作

    hist,bins = np.histogram(rollresult,bins=range(2,14)) #histogram输出直方图的统计结果
    print(hist)
    print(bins)

    #数据可视化
    plt.hist(rollresult,bins=range(2,14),density=1,edgecolor = 'black',linewidth = 1,rwidth=0.8) #这是画图
    #hist为直方图可视化方法，hist(data,bins) 纵坐标为数据，横坐标为区间。
    # density=1,表示将数据转化为概率表示，edgecolor = 'black',linewidth = 1 设置边框

    #将直方图的横坐标中文输出
    tick_lables = ['2点','3点','4点','5点','6点','7点','8点','9点','10点','11点','12点']

    tick_pos = np.arange(2,13)+0.5  #np.arange()生成一个[2,12]的数组，+0.5对数组中的每一个元素加0.5，结果为[2.5,3.5,……,12.5]
    plt.xticks(tick_pos,tick_lables) #设置X轴上文本标签的位置，xticks(元素位置，元素显示值)

    plt.title('筛子点数统计')
    plt.xlabel('点数')
    plt.ylabel('概率统计')
    plt.show()



if __name__ == '__main__':
    main()
