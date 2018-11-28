from selenium import webdriver
from time import sleep

'''读取txt文件'''

driver=webdriver.Firefox()
driver.get("http://192.168.1.101:7400/faext_s460")
def login():
    driver.find_element_by_xpath("//input[@id='textfield-1012-inputEl']").send_keys(username)
    sleep(2)
    driver.find_element_by_xpath("//input[@id='textfield-1013-inputEl']").send_keys(password)
    sleep(2)
    driver.find_element_by_xpath("//span[@id='button-1015-btnWrap']").click()
    sleep(2)
    driver.refresh()
'''
#使用read()读取文件 先用\n拆分出单行，每一行的数据再用"，"拆分出username和password
file = open('test data.txt')
lines = file.read()  #读取所有行的数据
file.close()

acountInfo = lines.split('\n')
print(acountInfo)

for l in acountInfo:
    username = l.split(',')[0]
    print(username)
    password = l.split(',')[1]
    print(password)
    login()
'''

'''
#使用readline()读取文件  readline()只读一行，
file = open('test data.txt')
lines=file.readline()
file.close()

acountinfo=lines.split('\n')
print(acountinfo)  #打印的结果是 ['root,111111', '']
print(acountinfo[0])  #打印的结果是 root,111111
acountinfo1 = acountinfo[0].split(',')
print(acountinfo1)  #打印的结果是['root', '111111']

username = acountinfo1[0]
print(username)
password = acountinfo1[1]
print(password)
login()



'''
#使用readlines()读取文件

file = open('test data.txt')
lines = file.readlines()   #读取所有行的数据，一行一行的进行读取
file.close()

for l in lines:
    print("l is ",l)
    
    
    username = l.split(',')[0]
    print (username)
    password = l.split(',')[1]
    print(password)
    login()


