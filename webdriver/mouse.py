from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")

'''
#鼠标右击
element=driver.find_element_by_id("su")
ActionChains(driver).context_click(element).perform()


driver.refresh()
time.sleep(1)

#鼠标悬停
element1=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(element1).perform()

time.sleep(1)

#鼠标双击
ActionChains(driver).double_click(driver.find_element_by_link_text("高级搜索")).perform()

driver.refresh()
time.sleep(1)
'''
'''
#鼠标拖放
#source=driver.find_element_by_link_text("新闻")
element=driver.find_element_by_name("tj_trnews")
target=driver.find_element_by_id("kw")

time.sleep(2)

action.clickAndHold(source).moveToElement(target).perform();
action.release(); 

ActionChains(driver).drag_and_drop(element,target).perform()

#target.submit()
'''
source=driver.find_element_by_link_text("新闻")
source.click()

time.sleep(2)

source=driver.find_element_by_link_text("帮助")

target=driver.find_element_by_xpath("//input[@id='ww']")
target.send_keys("haha")
#source.click()
ActionChains(driver).drag_and_drop(source,target).perform()





