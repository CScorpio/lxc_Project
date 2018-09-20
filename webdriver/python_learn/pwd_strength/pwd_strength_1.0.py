'''
功能：判断密码强度
'''
def is_exist_num(str):
    for i in str:
        if  i.isnumeric():  #isnumeric()判断字符串中是不是只含有数字
            return True
    return False

def is_exist_alpha(str):
    for i in str:
        if i.isalpha():   #isalpha()判断字符串中是不是只含有字母
            return True
    return False

def main():
    password_str = input("请输入密码")

    pwd_strength_count = 0
    #判断规则1：密码长度要大于8位
    if len(password_str) > 8:
        pwd_strength_count += 1
    else:
        print("请输入长度超过8位的密码")

    #判断规则2：密码中是否含有数字
    if is_exist_num(password_str) :
        pwd_strength_count += 1
    else:
        print("密码中需要包含数字")

    #判断规则3：密码中是否含有字母
    if is_exist_alpha(password_str):
        pwd_strength_count += 1
    else:
        print("密码中需要包含字母")

    if pwd_strength_count == 3:
        print("密码强度合格")
    else:
        print("密码强度不合格")


if __name__ == '__main__':
    main()