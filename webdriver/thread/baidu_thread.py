from selenium import webdriver
from time import ctime
import threading

def baidu_test(browser,value):
    print('当前时间是：',ctime())
    print('浏览器：',browser)
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()

    driver.get("https://www.baidu.com/")
    driver.find_element_by_id('kw').send_keys(value)
    driver.find_element_by_id('su').click()


list = {'chrome':'chrome浏览器','Firefox':'Firefox浏览器'}
#创建线程数组
threads = []
files = range(len(list))

for browser,value in list.items():
    t =  threading.Thread(target=baidu_test,args=(browser,value))
    threads.append(t)

if __name__ == '__main__':
    #启动线程
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

    print('end',ctime())

