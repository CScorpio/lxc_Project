'''
v4.0功能：可视化两个骰子的结果（直方图）
'''

import random
import matplotlib.pyplot as plt

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei'] #由于matplotlib默认支持输出英文，所以需要修改参数，输入字体为黑体
plt.rcParams['axes.unicode_minus'] = False

def rollDice():
    # 随机生成点数
    roll_result = random.randint(1, 6)
    #print("点数为：{}".format(roll_result))
    return roll_result

def main():
    '''
    投掷筛子
    '''
    #投掷筛子的次数
    roll_times = 1000

    rollresult = []


    for i in range(roll_times):
            result1 = rollDice()
            result2 = rollDice()

            rollresult.append(result1+result2)

    #数据可视化
    plt.hist(rollresult,bins=range(2,14),density=1,edgecolor = 'black',linewidth = 1)
    #hist为直方图可视化方法，hist(data,bins) 纵坐标为数据，横坐标为区间。
    # density=1,表示将数据转化为概率表示，edgecolor = 'black',linewidth = 1表示将边框的线设置为黑色并且宽度为1
    plt.title('筛子点数统计')
    plt.xlabel('点数')
    plt.ylabel('概率统计')
    plt.show()



if __name__ == '__main__':
    main()
