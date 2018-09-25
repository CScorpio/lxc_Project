'''
2.0功能：解析json文件
'''
import json

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
    top5_list = city_list[:5]

    f = open("yop5_aqi.json",'w',encoding='utf-8')
    json.dump(top5_list,f,ensure_ascii=False)  # 将python数据类型的数据输出到文件
                                               # json.dump()序列化时对中文默认使用的ascii编码，想输出真正的中文需要指定ensure_ascii = False
    f.close()
    print(city_list)


if __name__ == '__main__':
    main()