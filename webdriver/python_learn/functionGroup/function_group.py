'''
这是一个小功能组合：会将BMR、汇率兑换、存钱三个功能组合起来
'''

from python_learn.functionGroup import BMR
from python_learn.functionGroup import currency_converter
from python_learn.functionGroup import money_challenge

def main():
    function_selection = input("请选择您要使用的功能: 【1】BMR计算器 【2】汇率兑换 【3】存钱挑战")
    if function_selection == '1' :
        BMR.main()
    elif function_selection == '2':
        currency_converter.main()
    elif function_selection == '3':
        money_challenge.main()
    elif function_selection == 'end':
        print("退出程序")
    else:
        print('请重新选择功能')

if __name__ == '__main__':
    main()
