'''
8.0功能：将所获取的城市空气质量保存到csv文件中
'''
import json
import csv
import os
import requests
from bs4 import BeautifulSoup


def get_aqi_text(city_str):
    url = 'http://pm25.in/' + city_str
    page_html = requests.get(url,timeout = 30)
    #print(type(page_html.text))
    bs = BeautifulSoup(page_html.text,features="html.parser")
    all_div = bs.find_all('div',class_ = 'span1')
    #print(all_div)
    div_list = []
    for div in all_div:
        caption = div.find('div', class_='caption')
        if caption != None:
            caption = caption.text.strip() #strip()用于移除字符串头尾指定的字符或者字符序列
            #print(caption)
        value = div.find('div',class_ = 'value').text.strip()
        #div_list.append((caption,value))

        #在8.0版本中，不需要caption，只需要value就可以了
        div_list.append(value)

    return div_list

def get_city_name():
    url = 'http://pm25.in/'
    page_html = requests.get(url,timeout = 30)
    bs = BeautifulSoup(page_html.text,features='html.parser')

    all_city_div = bs.find_all('div',class_ = 'bottom')[1]
    #print(all_city_div[1])
    all_city_a = all_city_div.find_all('a')
    #print(all_city_a)
    city_list = []

    for city_a in all_city_a:
        city_name = city_a.text
        city_str = city_a['href'][1:]
        city_list.append((city_name,city_str))

    #print(city_list)
    return city_list


def main():
    city_msg =  get_city_name()
    #print(city_msg)


    '''
    #自己写的，但是有个问题，就是遍历出来div_list，每个值都是跨行输出的，看着不优雅
    header = ['city','AQI','PM2.5/1h','PM10/1h','CO/1h','NO2/1h','O3/1h','O3/8h','SO2/1h','other']
    f = open("all_city_aqi.csv",'w',encoding='utf-8',newline='')
    writer = csv.writer(f)
    writer.writerow(header)
    for city in city_msg:
        writer.writerow(city[0])
        city_str = city[1]
        div_list = get_aqi_text(city_str)
        for dl in div_list:
            writer.writerow(dl[1])
    f.close()
    '''
    #按照老师讲的来一遍 ,还是老师写的比较完整
    city_list = []
    header = ['city', 'AQI', 'PM2.5/1h', 'PM10/1h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h', 'other']
    with open("all_city_aqi.csv",'w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        # for city in city_msg:
        #数据量比较多，为了在处理数据的时候，可以更友好的让用户等待，可以这样写
        for i,city in enumerate(city_msg):
            if i%10 == 0:
                print("已经处理{}条数据（共{}条数据）".format(i,len(city_msg)))
            city_name = city[0]
            city_str = city[1]
            city_list.append((city_name, city_str))
            div_list = get_aqi_text(city_str)
            row = [city_name] + div_list  #city_name 是一个str，div_list是一个列表，如果想拼接起来，可以将city_name，变成一个列表[city_name]
            writer.writerow(row)


if __name__ == '__main__':
    main()