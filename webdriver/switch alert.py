from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Firefox()
driver.implicitly_wait(20)
driver.get("https://www.baidu.com/")

setting=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(setting).perform()

search_setting = driver.find_element_by_link_text("搜索设置")
ActionChains(driver).double_click(search_setting).perform()


save_setting = driver.find_element_by_link_text("保存设置")
save_setting.click()

aa=driver.switch_to_alert().text #返回警告框中的文本信息
print(aa)
#driver.switch_to_alert().accept() #接受现有警告框
driver.switch_to_alert().dismiss() #解散现有警告框
#driver.switch_to_alert().send_keys(keysToSend='sss') #发送文本至警告框
