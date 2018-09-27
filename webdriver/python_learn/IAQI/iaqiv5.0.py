'''
5.0功能：爬虫获取某个城市的aqi值
'''
import json
import csv
import os
import requests


def get_html_text(url):
    page_html = requests.get(url,timeout = 30)
    # print(page_html.status_code)
    # print(page_html.text)
    # print(page_html)
    return page_html.text



def main():
    city_str = input('请输入要查询的城市')
    url = 'http://pm25.in/' + city_str
    page_html = get_html_text(url)


    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = page_html.find(aqi_div)  #从页面的html文本中找到aqi存在的value的索引值
    start_index = index + len(aqi_div)
    end_index = start_index + 2


    aqi = page_html[start_index:end_index]
    print(aqi)




if __name__ == '__main__':
    main()