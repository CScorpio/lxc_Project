'''
3.0新增功能，(1)将汇率兑换功能封装到函数中  (2)
'''


def convert_convercy(va,e_rate):
    '''
    计算费率的函数
    '''
    return va*e_rate

def main():

    #汇率
    USD_VS_RMB = 6.77  #常量需要用大写标识



    # 人民币的输入
    currency_str_value = input('请输入带单位的货币金额:')
    while currency_str_value != 'end':

        if len(currency_str_value) <= 3:
            print('请输入金额+单位')
        else:
            # 取出输入字符串的后三位作为货币金额的单位
            unit = currency_str_value[-3:]

            #对汇率进行转换
            if unit == 'CNY':
                exchange_rate = 1/USD_VS_RMB
            elif unit == 'USD':
                exchange_rate = USD_VS_RMB
            else:
                exchange_rate = -1

            if exchange_rate != -1:
                value = eval(currency_str_value[:-3])
                result = convert_convercy(value,exchange_rate)
                print(result)
            else:
                print("不支持这种类型的汇率")

        currency_str_value = input('请输入带单位的货币金额:')

    print('程序已退出')

if __name__ == '__main__':
    main()




