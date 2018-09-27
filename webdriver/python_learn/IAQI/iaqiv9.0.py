'''
9.0功能：引用pandas包，对数据进行处理和分析
'''
import pandas as pd

def main():
    '''
    ser_obj = pd.Series(range(10,20))
    print(ser_obj)

    #输出该数据的索引
    print(ser_obj.index)
    #输出该数据的值
    print(ser_obj.values)
    #预览数据,head中的数字代表预览几行
    print(ser_obj.head(5))

    #通过索引获取数据
    print(ser_obj[6])
    '''
    aqi_data = pd.read_csv('all_city_aqi.csv')
    print("基本信息：")
    print(aqi_data.info())  #输出文件的基本信息

    print("数据预览：")
    print(aqi_data.head())  #输出文化预览信息


    #基本统计
    print("AQI的最大值：",aqi_data['AQI'].max())
    print("AQI的最小值",aqi_data['AQI'].min())
    print("AQI的平均值",aqi_data['AQI'].mean())

    #空气质量最好的前10个城市
    top10 = aqi_data.sort_values('AQI').head(10)  #排序时，默认从小到大进行排序
    print(top10)
    #空气质量最差的前10个城市
    bottom10 = aqi_data.sort_values('AQI',ascending=False).head(10) #当ascending = False 时，排序默认从大到小进行排序
    #另外一种写法
    #bottom10 = aqi_data.sort_values('AQI').tail(10) #从小到大排序后，倒数10个数
    print(bottom10)

    #保存到csv文件中
    top10.to_csv('top10_aqi_cites.csv',index = False)  #pandas中to_csv()方法直接将一个数据保存到csv文件中，保存时，默认会带着索引，
    bottom10.to_csv('bottom10_aqi_cites.csv',index = False) #当index  = False时，会把索引去掉进行保存




if __name__ == '__main__':
    main()