'''
v2.0功能：投掷两个骰子，投掷点数以及计算点数的概率
'''

import random

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
    roll_times = 1000000


    #记录点数生成的次数
    roll_times_list = [0] * 11

    #初始化点数列表
    roll_list = list(range(2,13))

    print(zip(roll_times_list,roll_list))
    roll_dict = dict(zip(roll_list,roll_times_list)) #注意zip()转化为字典时，由于字典的键值必须唯一，所以要将点数放在前面。否则，roll_dict = {0:12}
    print('********',roll_dict)

    for i in range(roll_times):

            result1 = rollDice()
            result2 = rollDice()

            for j in range(2,13):
                if (result1+result2) == j:
                    roll_dict[j] += 1  #这句话是字典的赋值语句，即根据字典的键，赋值给该键对应的值


    for i,result in roll_dict.items():
        print("点数为{}的次数为{}，频率为{}".format(i,result,result/roll_times))


if __name__ == '__main__':
    main()
