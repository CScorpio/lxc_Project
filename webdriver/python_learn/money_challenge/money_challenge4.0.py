'''
新增功能：灵活设置周数，存钱金额数，变成用户可输入的，并且循环体用函数进行封装
'''

import math

saving = 0

def savingMoney(monney_per_week,increase_money,total_week):

    global saving
    list = []  # 每周存款数的列表

    for i in range(total_week):
        list.append(monney_per_week)
        saving = math.fsum(list)

        print('第{}周，存入{}元，账户累计{}元'.format(i + 1,monney_per_week,saving))

        #更新下一周的存钱金额
        monney_per_week +=  increase_money
        #i += 1
    print(list)
    print('***',saving)
    return saving


def main():

    input_msg = input('请输入每周存入的金额，每周递增的金额，周数（用空格进行区分）：')
    input_list = input_msg.split(' ')
    print(input_list)

    monney_per_week = float(input_list[0])
    increase_money = float(input_list[1])
    total_week = int(input_list[2])
    savingMoney(monney_per_week,increase_money,total_week)
    print('***',saving)


if __name__ == '__main__':
    main()


