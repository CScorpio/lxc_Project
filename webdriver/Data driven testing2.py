import csv
from selenium import webdriver
from time import sleep
'''读取csv文件'''

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



data = csv.reader(open('data.csv'))
print(data)

for i in data:
    print(i)
    username = i[0]
    print('username is :'+username)
    password = i[1]
    print('password is :'+password)
    login()

