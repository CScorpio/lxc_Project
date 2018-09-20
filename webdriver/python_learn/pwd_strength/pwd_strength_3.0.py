'''
功能：将密码以及密码强度保存到文件中
'''
def is_exist_num(str):

    has_number  = False

    for i in str:
        if  i.isnumeric():  #isnumeric()判断字符串中是不是只含有数字
            has_number = True
            break

    return has_number

def is_exist_alpha(str):
    has_alpha = False

    for i in str:
        if i.isalpha():   #isalpha()判断字符串中是不是只含有字母
            has_alpha = True
            break

    return has_alpha

def main():

    times = 5

    while times >0:
        pwd_strength_count = 0
        password_str = input("请输入密码")


        #判断规则1：密码长度要大于8位
        if len(password_str) > 8:
            pwd_strength_count += 1
        else:
            print("请输入长度超过8位的密码")

        #判断规则2：密码中是否含有数字
        if is_exist_num(password_str):
            pwd_strength_count += 1
        else:
            print("密码中需要包含数字")

        #判断规则3：密码中是否含有字母
        if is_exist_alpha(password_str):
            pwd_strength_count += 1
        else:
            print("密码中需要包含字母")

        if pwd_strength_count == 3:
            pwd_strength = "强"
        elif pwd_strength_count == 2:
            pwd_strength = "中"
        else:
            pwd_strength = "弱"

        f = open('pwd_strength_3.0.txt', 'a')
        f.write('密码：{}，强度：{} \n'.format(password_str,pwd_strength))
        f.close()

        if pwd_strength_count == 3:
            print("密码强度合格")
            break
        else:
            print("密码强度不合格")
            times -= 1

        print()

    if times <= 0:
        print("输入密码次数超过5，程序退出")


if __name__ == '__main__':
    main()