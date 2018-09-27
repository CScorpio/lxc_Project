'''
10.0功能：对数据进行清洗和可视化显示
'''
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def main():

    aqi_data = pd.read_csv('all_city_aqi.csv')
    print("基本信息：")
    print(aqi_data.info())  #输出文件的基本信息

    print("数据预览：")
    print(aqi_data.head())  #输出文化预览信息

    #清洗数据
    filter_condition = aqi_data['AQI'] > 0
    clean_aqi_data = aqi_data[filter_condition]


    #基本统计
    print("AQI的最大值：",clean_aqi_data['AQI'].max())
    print("AQI的最小值",clean_aqi_data['AQI'].min())
    print("AQI的平均值",clean_aqi_data['AQI'].mean())

    #空气质量最好的前10个城市
    top10 = clean_aqi_data.sort_values('AQI').head(10)  #排序时，默认从小到大进行排序
    print(top10)
    #空气质量最差的前10个城市
    bottom10 = clean_aqi_data.sort_values('AQI',ascending=False).head(10) #当ascending = False 时，排序默认从大到小进行排序
    #另外一种写法
    #bottom10 = clean_aqi_data.sort_values('AQI').tail(10) #从小到大排序后，倒数10个数
    print(bottom10)

    #可视化结果
    top50 = clean_aqi_data.sort_values('AQI').head(50)  # 排序时，默认从小到大进行排序
    top50.plot(kind = 'bar',x='city',y = 'AQI' ,title = '空气质量最好的50个城市',figsize = (20,10)) #figsize设置图片的大小
    plt.savefig('top50_aqi_bar.png') #需要先进性保存，然后再show()
    plt.show()








if __name__ == '__main__':
    main()