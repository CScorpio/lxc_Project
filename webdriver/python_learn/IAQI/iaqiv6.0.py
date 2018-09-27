'''
6.0功能：beautifulsoup4,输出所有城市的aqi值
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
        div_list.append((caption,value))

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
    for city in city_msg:
        city_name = city[0]
        city_str = city[1]
        div_list = get_aqi_text(city_str)
        print(city_name,div_list)




if __name__ == '__main__':
    main()