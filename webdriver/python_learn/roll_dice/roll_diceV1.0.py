'''
v1.0功能：投掷一个筛子，计算投掷点数的概率
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
    roll_times = 100


    #记录点数生成的次数
    roll_times_list = [0] * 6

    for i in range(roll_times):
        roll_times_list[rollDice() - 1] += 1


    print(roll_times_list)
    print(enumerate(roll_times_list))

    for i,result in enumerate(roll_times_list):     #用i去遍历列表，i为列表中的元素，而不是索引，所以在下面循环体中，
                                                    # 假如生成的roll_times_list为[23, 19, 13, 13, 10, 22]
                                                    # roll_times_list[i]为索引23的元素。但是元素中只有6个，所以此时需要函数enumerate()
        print("点数为{}的次数为{}，频率为{}".format(i+1,result,result/roll_times))


if __name__ == '__main__':
    main()









'''
练习：
    l = list(range(0,10))
    print(l)

    a = random.random() #随机生成0-1之间的一个浮点数
    print(a)
    b = random.uniform(1,10) #随机生成1-10之间的一个浮点数
    print(b)
    c = random.randint(1,10) #随机生成一个1-10之间的整数
    print(c)
    d = random.choice(l)  #从列表中随机返回一个元素
    print(d)
    random.shuffle(l) #将列表中的元素随机打乱  由于shuffle没有返回值，所以e接收不到，print（e）为一个none
    print(l)
    e =  random.sample(l,3) #随机从指定的列表中获取k个元素
    print(e)
'''