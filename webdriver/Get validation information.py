from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")

#打印当前页面的title
print(driver.title)
#打印当前页面的url
print(driver.current_url)

driver.find_element_by_link_text("登录").click()
time.sleep(2)

driver.find_element_by_xpath("//p[@title='用户名登录']").click()
time.sleep(2)

driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("亦茉prince")
driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("cpk1991121215")
driver.find_element_by_id("TANGRAM__PSP_10__password").submit()

#打印当前页面的title
print(driver.title)
#打印当前页面的url
print(driver.current_url)