

def main():
    monney_per_week = 10 #每周存入的金额
    i=1 #周数
    increase_money = 10 #每周递增的金额
    total_week = 52 #总共的周数
    saving = 0  #账户中的金额

    while i <=  total_week:
        saving += monney_per_week

        print('第{}周，存入{}元，账户累计{}元'.format(i,monney_per_week,saving))

        #更新下一周的存钱金额
        monney_per_week +=  increase_money
        i += 1



if __name__ == '__main__':
    main()