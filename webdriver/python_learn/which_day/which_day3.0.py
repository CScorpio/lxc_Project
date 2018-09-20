'''
功能新增：用集合替换列表


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

    days_sum = day


    #包含30天的月份集合
    _30_month_days = [4,6,9,11]
    _31_month_days = [1,3,5,7,8,10,12]

    for i in range(1,month):

        if i in _30_month_days:
            days_sum += 30
        elif i in _31_month_days:
            days_sum += 31
        else:
            days_sum +=28

    if is_leap_year(year) and month>2:
        days_sum +=1



    print('您输入的日期{}是当年的第{}天'.format(input_date_str,days_sum))


if __name__ == '__main__':
    main()