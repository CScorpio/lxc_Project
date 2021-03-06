'''
功能新增：用列表替换元祖


'''
from datetime import datetime


def is_leap_year(year):
    '''判断year是否为闰年，是，返回true，否返回false'''

    is_leap = False

    if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):  #可以用if else语句用两个return，但是这样的程序会不够优雅
        return True

    return is_leap

def main():

    #根据用户输入的字符串转化为日期格式的数据
    input_date_str = input('请输入日期(yyyy-mm-dd)：')
    input_date = datetime.strptime(input_date_str,'%Y-%m-%d')


    #获得年月日
    year = input_date.year
    month = input_date.month
    day = input_date.day

    #将每个月的日期存入元祖tuple
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year):
        days[1] = 29
    #计算月的天数
    month_sum = sum(days[:month-1])

    #加上天的天数
    days_sum = month_sum + day


    print('您输入的日期{}是当年的第{}天'.format(input_date_str,days_sum))


if __name__ == '__main__':
    main()