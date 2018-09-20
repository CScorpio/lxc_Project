'''
新增功能：根据用户输入的日期，判断第几周，并且输出用户的存款金额
'''

import math
import datetime

saving = 0

def savingMoney(monney_per_week,increase_money,total_week):

    global saving
    list = []  # 每周存款数的列表
    sava_money_list = [] #记录每周账户累计金额

    for i in range(total_week):
        list.append(monney_per_week)
        saving = math.fsum(list)
        sava_money_list.append(saving)

        print('第{}周，存入{}元，账户累计{}元'.format(i + 1,monney_per_week,saving))

        #更新下一周的存钱金额
        monney_per_week +=  increase_money
        #i += 1
    print(list)
    print('***',saving)
    return sava_money_list


def main():

    input_msg = input('请输入每周存入的金额，每周递增的金额，周数（用空格进行区分）：')
    input_list = input_msg.split(' ')
    print(input_list)

    monney_per_week = float(input_list[0])
    increase_money = float(input_list[1])
    total_week = int(input_list[2])
    sava_money_list = savingMoney(monney_per_week,increase_money,total_week)

    input_date_str = input('请输入日期（yyyy/mm/dd）:')
    inputdate = datetime.datetime.strptime(input_date_str,'%Y/%m/%d') #将字符串类型解析成datetime类型 strftime()会将datetime类型转化为字符串
    week_num = inputdate.isocalendar()[1] #isocalendar()这个方法返回一个元组，年，周数，以及周几

    print('第{}周的存款是{}元'.format(week_num,sava_money_list[week_num-1]))
    print('***',saving)


if __name__ == '__main__':
    main()


