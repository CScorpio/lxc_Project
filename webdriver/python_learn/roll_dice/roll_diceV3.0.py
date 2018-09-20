'''
v3.0功能：可视化投掷两个筛子结果(散点图绘制)
'''

import random
import matplotlib.pyplot as plt

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


    #记录点数生成的次数
    roll_times_list = [0] * 11

    #初始化点数列表
    roll_list = list(range(2,13))

    print(zip(roll_times_list,roll_list))
    roll_dict = dict(zip(roll_list,roll_times_list)) #注意zip()转化为字典时，由于字典的键值必须唯一，所以要将点数放在前面。否则，roll_dict = {0:12}
    print('********',roll_dict)

    rollresult1 = []
    rollresult2 = []


    for i in range(roll_times):

            result1 = rollDice()
            rollresult1.append(result1)
            result2 = rollDice()
            rollresult2.append(result2)

            for j in range(2,13):
                if (result1+result2) == j:
                    roll_dict[j] += 1  #这句话是字典的赋值语句，即根据字典的键，赋值给该键对应的值


    for i,result in roll_dict.items():
        print("点数为{}的次数为{}，频率为{}".format(i,result,result/roll_times))

    #数据可视化
    x = list(range(1,roll_times+1))
    plt.scatter(x,rollresult1,c='red',alpha=0.5)
    plt.scatter(x,rollresult2,c='green',alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()
