from selenium import webdriver
from time import sleep

'''参数化搜索关键字'''

Text = ['李晓晨','谢瑶瑶','陈梦玲']

for text in Text:
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com/")
    driver.find_element_by_id("kw").send_keys(text)
    driver.find_element_by_id("su").click()
    sleep(2)
    print(text)


