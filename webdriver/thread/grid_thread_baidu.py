from time import ctime,sleep
from selenium import webdriver
import threading


#测试用例
def test_baidu(host,browser):
    print(ctime())
    print(host,browser)
    dc = {'browserName:',browser}
    driver  =  webdriver.Remote(command_executor=host,
                                desired_capabilities=dc)
    driver.get("https://www.baidu.com/")
    driver.find_element_by_id('kw').send_keys(browser)
    driver.find_element_by_id('su').click()

if __name__ == '__main__':
    #启动参数（指定运行主机与浏览器）
    lists = {'http://127.0.0.1:4444/wd/hub':'chrome',
             'http://127.0.0.1:5555/wd/hub':'firefox'}

    thread = []

    for host,browser in lists.items():
        t = threading.Thread(target=test_baidu,args=(host,browser))
        thread.append(t)

    file = range(len(lists))

    #启动线程
    for i in file:
        thread[i].start()
    for i in file:
        thread[i].join()

    print('end:',ctime())
