'''
功能：BMR计算器
日期：20180910
功能：一次输入所有的信息
'''





def main():

    y_or_n = input('是否退出程序（Y/N）？')

    while y_or_n == 'N':
        '''
        #性别
        gender = input('请输入性别：')
        #体重kg
        weight = float(input('请输入体重(kg)：'))
        #身高cm
        height = float(input('请输入身高(cm)：'))
        #年龄
        age = int(input('请输入年龄：'))
        '''
        print('请输入一下信息：用空格分隔')
        input_str = input('性别 体重（kg） 身高（gm） 年龄')

        list = input_str.split(' ')
        gender = list[0]
        weight = float(list[1])
        height = float(list[2])
        age = int(list[3])

        if gender == '男':
            #男性
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age +66)
        elif gender == '女':
            #女性
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('您的性别：{}，体重：{}公斤，身高：{}厘米，年龄：{}岁'.format(gender,weight,height,age))
            print('您的性别：{0}，体重：{1}公斤，年龄：{3}岁,身高：{2}厘米'.format(gender,weight,height,age)) #可以标记顺序
            print('您的基础代谢率:{}大卡'.format(bmr))

        else:
            print('暂不支持该性别')

        y_or_n = input('是否退出程序（Y/N）？')




if __name__ == '__main__':
    main()