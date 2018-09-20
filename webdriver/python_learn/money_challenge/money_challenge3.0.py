'''
新增功能：使用循环直接计数
'''



import math


def main():
    monney_per_week = 10 #每周存入的金额
    increase_money = 10 #每周递增的金额
    total_week = 52 #总共的周数
    saving = 0  #账户中的金额
    list=[]  #每周存款数的列表


    for i in range(total_week):

        list.append(monney_per_week)
        saving = math.fsum(list)

        print('第{}周，存入{}元，账户累计{}元'.format(i + 1,monney_per_week,saving))

        #更新下一周的存钱金额
        monney_per_week +=  increase_money
        #i += 1
    print(list)


if __name__ == '__main__':
    main()