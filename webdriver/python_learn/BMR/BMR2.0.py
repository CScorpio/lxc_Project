'''
功能：BMR计算器
日期：20180910
功能：增加输入，并且一直输入，直到用户输入停止
'''





def main():

    y_or_n = input('是否退出程序（Y/N）？')

    while y_or_n == 'N':

        #性别
        gender = input('请输入性别：')
        #体重kg
        weight = float(input('请输入体重(kg)：'))
        #身高cm
        height = float(input('请输入身高(cm)：'))
        #年龄
        age = int(input('请输入年龄：'))


        if gender == '男':
            #男性
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age +66)
        elif gender == '女':
            #女性
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('基础代谢率:',bmr)

        else:
            print('暂不支持该性别')

        y_or_n = input('是否退出程序（Y/N）？')




if __name__ == '__main__':
    main()