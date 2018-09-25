
def cal_iaqi_result(iaqi_hi,iaqi_lo,bp_hi,bp_lo,cp):

    IAQI = (iaqi_hi - iaqi_lo) * (cp - bp_lo) /(bp_hi-bp_lo) + iaqi_lo
    return IAQI




def cal_pm_iaqi(pm_param):
    '''
    计算pm2.5的IAQI
    '''
    pm_iaqi_result = 0

    if  0 <= pm_param < 36:
        pm_iaqi_result = cal_iaqi_result(50, 0, 35, 0, pm_param)
    elif 36 <= pm_param < 76:
        pm_iaqi_result = cal_iaqi_result(100, 50, 75, 35, pm_param)
    elif 76 <= pm_param < 116:
        pm_iaqi_result = cal_iaqi_result(150,100,115,75,pm_param)
    elif  116 <= pm_param < 151:
        pm_iaqi_result = cal_iaqi_result(200,150,150,115,pm_param)
    elif  151 <= pm_param < 251:
        pm_iaqi_result = cal_iaqi_result(300,200,250,150,pm_param)
    elif 251 <= pm_param < 351:
        pm_iaqi_result = cal_iaqi_result(400,300,350,250,pm_param)
    elif 351 <= pm_param < 500:
        pm_iaqi_result = cal_iaqi_result(500,400,500,350,pm_param)
    else:
        print('您输入的污染物浓度值不合理')

    return pm_iaqi_result


def cal_co_iaqi(co_param):
    '''
    计算CO的IAQI
    '''
    co_iaqi_result = 0

    if  0 <= co_param < 36:
        co_iaqi_result = cal_iaqi_result(50, 0, 2, 0, co_param)
    elif 36 <= co_param < 76:
        co_iaqi_result = cal_iaqi_result(100, 50, 4, 2, co_param)
    elif 76 <= co_param < 116:
        co_iaqi_result = cal_iaqi_result(150,100,14,4,co_param)
    elif  116 <= co_param < 151:
        co_iaqi_result = cal_iaqi_result(200,150,24,14,co_param)
    elif  151 <= co_param < 251:
        co_iaqi_result = cal_iaqi_result(300,200,36,24,co_param)
    elif 251 <= co_param < 351:
        co_iaqi_result = cal_iaqi_result(400,300,48,36,co_param)
    elif 351 <= co_param < 500:
        co_iaqi_result = cal_iaqi_result(500,400,60,48,co_param)
    else:
        print('您输入的污染物浓度值不合理')

    return co_iaqi_result



def AQI(param_list):

    pm_param = param_list[0]
    co_param = param_list[1]

    pm_iaqi = cal_pm_iaqi(pm_param)
    co_iaqi = cal_co_iaqi(co_param)

    IAQI_list = []
    IAQI_list.append(pm_iaqi)
    IAQI_list.append(co_iaqi)

    aqi_result = max(IAQI_list)
    return aqi_result


def main():
    #用户输入
    print("请输入以下信息，用空格进行分隔")
    input_str = input("(1)PM2.5 (2)CO :")
    input_list = input_str.split(' ')
    print(input_list)
    pm_param = float(input_list[0])
    co_param = float(input_list[1])


    #需要一个列表存放值，用来计算最后结果
    AQI_result = []
    AQI_result.append(pm_param)
    AQI_result.append(co_param)
    print(AQI_result)

    #调用计算AQI的方法

    result = AQI(AQI_result)
    print("空气质量指数为：{}".format(result))


if __name__ == '__main__':
    main()