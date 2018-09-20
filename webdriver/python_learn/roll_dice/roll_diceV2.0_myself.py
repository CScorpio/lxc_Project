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
    roll_times = 10


    #记录点数生成的次数
    roll_times_list = [0] * 11

    for i in range(roll_times):

            result1 = rollDice()
            #print('第一个筛子的点数为：{}'.format(result1))
            result2 = rollDice()
            #print('第二个筛子的点数为：{}'.format(result2))
            #print('第{}次的点数和：{}'.format(i,result1+result2))
            roll_times_list[result1+result2-2] += 1


    print(roll_times_list)
    #print(enumerate(roll_times_list))

    for i,result in enumerate(roll_times_list):
        print("点数为{}的次数为{}，频率为{}".format(i+2,result,result/roll_times))


if __name__ == '__main__':
    main()
