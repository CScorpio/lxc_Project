from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os

driver=webdriver.Firefox()
print(driver)
file_path='file:///'+os.path.abspath("frame.html")
driver.get(file_path)

#需要切换到iframe
#driver.switch_to.frame('if')
#driver.switch_to.frame("nf") #swith_to,frame()默认可以直接取表单的id或者name属性

'''
如果没有id和name属性，可以先通过其他属性进行定位，再将定位的对象传给switch_to.frame
'''
f = driver.find_element_by_xpath("//iframe[@id='if']")
driver.switch_to.frame(f)


driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()

#driver.switch_to.parent_frame()#该swich_to.parent_frame()方法默认跳出对应于离他最近的
driver.switch_to.default_content()#多级表单的情况下，跳回最外层的页面

try:
    driver.find_element_by_id("kw")
except NoSuchElementException as msg:
    print(msg,'跳出当前表单后，找不到百度输入框')
