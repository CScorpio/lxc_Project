from selenium import webdriver
import time
driver =  webdriver.Firefox()
driver.get("https://www.baidu.com/")

print("设置浏览器宽480，高400显示")
driver.set_window_size(480,800)
driver.find_element_by_link_text("登录").click()
print("设置浏览器全屏显示")
driver.maximize_window()
time.sleep(2)
#driver.back()
 #driver.forward()
#driver.refresh()



driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
driver.find_element_by_css_selector("input#TANGRAM__PSP_10__userName").send_keys("亦茉prince")
#driver.find_element_by_css_selector("input#TANGRAM__PSP_10__userName").clear()
driver.find_element_by_css_selector("input#TANGRAM__PSP_10__password").send_keys("cpk1991121215")
driver.find_element_by_css_selector("input#TANGRAM__PSP_10__password").submit()
#driver.find_element_by_css_selector("input#TANGRAM__PSP_10__submit").click()
time.sleep(2)
driver.refresh()

driver.find_element_by_id("kw").send_keys("闫梦彪 ")
driver.find_element_by_id("kw").submit()

time.sleep(1)

driver.back()

'''
print("cp is display:",driver.find_element_by_id("cp").is_displayed())
cp=driver.find_element_by_id("cp")
print ("cp")
print(cp.size)
print(cp.text)
'''

driver.refresh()
time.sleep(1)

size=driver.find_element_by_id("kw").size
print(size)

text=driver.find_element_by_id("cp").text
print(text)



attribute= driver.find_element_by_id("kw").get_attribute('name')
print(attribute)

isdisplay=driver.find_element_by_id("kw").is_displayed()
print(isdisplay)






