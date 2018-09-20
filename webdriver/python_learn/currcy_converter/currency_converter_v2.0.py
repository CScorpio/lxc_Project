'''
2.0新增功能:根据输入判断是人民币还是美元，进行相应的转换计算
2.0新增功能：程序可以一直运行，知道用户选择退出
'''

#汇率
USD_VS_RMB = 6.77  #常量需要用大写标识
i = 0

while True:
    i = i + 1
    print('****************************************')
    print('当前是第：', i,'次循环')
    result = ''
    # 人民币的输入
    currency_str_value = input('请输入带单位的货币金额:')
    if currency_str_value == 'end':
        break
    else:
        if len(currency_str_value) <= 3:
            print('请输入金额+单位')
        else:
            # 取出输入字符串的后三位作为货币金额的单位
            unit = currency_str_value[-3:]
            value = eval(currency_str_value[:-3])
            if unit == 'CNY':
                result = value/USD_VS_RMB
            elif unit == 'USD':
                result = value*USD_VS_RMB
            else:
                print("暂时不支持这种金额 或者 输入有误，请重新输入")

            print(result)

