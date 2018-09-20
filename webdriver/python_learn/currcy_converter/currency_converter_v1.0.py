

#汇率
USD_VS_RMB = 6.77  #常量需要用大写标识

#人民币的输入
rmb_str_value = input('请输入人民币(CNY)金额:')
#将字符串转换为数字
rmb_value = eval(rmb_str_value)

#汇率的计算
usd_value = rmb_value/USD_VS_RMB
#usd_value = float(rmb_str_value)/usd_vs_rmb

#输出结果
print(rmb_str_value)
print('美元(USD)金额是：', usd_value)
