'''
4.0功能：通过判断后缀名，根据文件类型来读文件
'''
import json
import csv
import os


def process_json_file(file_path): #解码json文件
    # f = open(file_path,'r',encoding='UTF-8') #用只读打开文件，并且编码格式为utf-8
    # city_list = json.load(f)  #将json格式字符串转换为python数据类型，从文件读入
    # f.close()
    # return city_list

    with open(file_path,'r',encoding='UTF-8') as f: #使用with，不管在处理文件过程中是否发生异常，都能保证with语句执行完毕后关闭文件，不需要close语句
        city_list = json.load(f)
    print(city_list)


def process_csv_file(file_path): #处理csv文件

    with open(file_path,'r',encoding='UTF-8',newline='') as f:
        reader = csv.reader(f)
        for row in reader:        #通过遍历获取每一行的列表元素
            #print(row)
            print(','.join(row))   #可以将列表中的元素用，分隔显示
    

def main():

    file_path = input("请输入文件的路径：")
    file_name,file_ext = os.path.splitext(file_path) #os.path.splitext()该方法可以将文件全称分隔成文件名称和后缀名称
    if file_ext ==  '.json':
        process_json_file(file_path)
    elif file_ext == '.csv':
        process_csv_file(file_path)
    else:
        print("不支持该种文件类型")



if __name__ == '__main__':
    main()