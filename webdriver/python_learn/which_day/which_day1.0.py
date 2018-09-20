'''
功能：输入任意一天，来判断输入的天是今天的第几天
功能分析：

'''
from datetime import datetime

def main():

    #根据用户输入的字符串转化为日期格式的数据
    input_date_str = input('请输入日期(yyyy-mm-dd)：')
    input_date = datetime.strptime(input_date_str,'%Y-%m-%d')


    #获得年月日
    year = input_date.year
    month = input_date.month
    day = input_date.day

    #将每个月的日期存入元祖tuple
    days = (31,28,31,30,31,30,31,31,30,31,30,31)

    #计算月的天数
    month_sum = sum(days[:month-1])

    #加上天的天数
    days_sum = month_sum + day

    #判断如果是闰年，则2月加1
    if (year % 400 == 0) or ((year%100!=0)and(year%4==0)):
        if(month > 2):
            days_sum +=1

    print('您输入的日期{}是今年的第{}天'.format(input_date_str,days_sum))


if __name__ == '__main__':
    main()