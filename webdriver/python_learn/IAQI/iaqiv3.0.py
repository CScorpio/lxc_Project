'''
3.0功能：解析csv文件
'''
import json
import csv

def xxx(city):
    return city['aqi']


def process_file(file_path): #解码json文件
    f = open(file_path,'r',encoding='UTF-8') #用只读打开文件，并且编码格式为utf-8
    city_list = json.load(f)  #将json格式字符串转换为python数据类型，从文件读入
    f.close()
    return city_list

def main():
    file_path = input("请输入json文件的路径：")
    city_list = process_file(file_path)

    #city_list.sort(key = lambda city:city['aqi']) #city在列表中表示键值对数据组成的对象，city['aqi']表示这个对象中，键为aqi的的值
                                                  #lambda city:city['aqi']返回了 键为aqi的的值
                                                  #sort(key = lambda city:city['aqi'])表示按照key = aqi的值进行的排序，默认从小到大排序

    city_list.sort(key = xxx)

    line = [] #新建一个空的列表，用于存放读取到的数据
    line.append(city_list[0].keys()) #第一行，存放的是city_list中的键,即表头

    #遍历city_list，把每个键值对组成的对象中的值存档到line中
    for city in city_list:
        line.append(city.values()) #问题2：老师写的时候，line.append(list(city.values()))，但是我不转貌似也没有毛病啊
    print(line)

    #将列表中的元素写入csv文件中
    f = open('aqi.csv','w',encoding='utf-8',newline='')
    writer = csv.writer(f)
    for l in line:
        writer.writerow(l)
    f.close()


if __name__ == '__main__':
    main()