'''
新增功能：根据用户输入的日期，判断是一年中的第几周，然后输出相应的存款金额
'''
import datetime

import math




def saveMoney(monney_per_week,increase_money,total_week,current_week):

    list = []  # 每周存款数的列表

    for i in range(total_week):
        list.append(monney_per_week)
        save_sum = math.fsum(list)

        if i == int(current_week):
            print('您查询的结果是：第{}周的存入{}元，现在账户中共有{}元：'.format(i,monney_per_week,save_sum))

        # 更新下一周的存钱金额
        monney_per_week += increase_money



def input_date(year,mouth,day):

    date = datetime.date(year,mouth,day)  # datetime.date(year,mounth,day) 返回一个日期对象
    datemsg = date.isocalendar() #这方法返回一个元祖，包括（年，一年中的第几周，以及在一周中的第几天）

    print('今年是{}年，是一年中的第{}周'.format(datemsg[0],datemsg[1]))
    return datemsg[1]


def main():

    input_msg = input('请输入每周存入的金额，每周递增的金额，周数（用空格进行区分）：')
    input_list = input_msg.split(' ')
    monney_per_week = float(input_list[0])
    increase_money = float(input_list[1])
    total_week = int(input_list[2])


    inputdate = input('请输入要查询的日期，年 月 日（用空格进行区分）：')
    datetime = inputdate.split(' ')
    year = int(datetime[0])
    mouth = int(datetime[1])
    day = int(datetime[2])
    weeknum = input_date(year,mouth,day)
    saveMoney(monney_per_week, increase_money, total_week,weeknum)


if __name__ == '__main__':
    main()


