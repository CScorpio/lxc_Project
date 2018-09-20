from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
'''
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

driver.set_window_size(600,600)

time.sleep(2)

js='window.scrollTo(100,450);'
driver.execute_script(js)
'''
text="input text"
js="var sum=document.getElementById('kw'); sum.value = '" + text + "'; "
driver.execute_script(js)

