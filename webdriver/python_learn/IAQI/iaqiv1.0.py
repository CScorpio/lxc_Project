

def cal_pm_aqi(pm_param):
    pass

def cal_co_aqi(co_param):
    pass



def AQI(param_list):

    pm_param = param_list[0]
    co_param = param_list[1]

    pm_aqi = cal_pm_aqi(pm_param)
    co_aqi = cal_co_aqi(co_param)

    l = []
    l.append(pm_aqi)
    l.append(co_aqi)

    aqi_result = max(l)
    return aqi_result


def main():
    #用户输入
    print("请输入一下信息，用空格进行分隔")
    input_str = input("(1)PM2.5 (2)CO :")
    input_list = input_str.split(' ')
    pm_param = float(input_list[0])
    co_param = float(input_list[1])


    #需要一个列表存放值，用来计算最后结果
    AQI_result = []
    AQI_result.append(pm_param)
    AQI_result.append(co_param)

    #调用计算AQI的方法
    result = AQI(AQI_result)
    print("空气质量指数为：{}".format(result))


if __name__ == '__main__':
    main()