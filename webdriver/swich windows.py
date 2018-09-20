from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com/")

#获得百度搜索窗口句柄
search_window=driver.current_window_handle  #获取当前窗口句柄
print(search_window)

driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("立即注册").click()

time.sleep(2)
print(driver.current_window_handle+"kkkkk") #页面跳转后，当前句柄没有发生改变
#获得当前所有打开的窗口的句柄
all_handles=driver.window_handles  #获取当前打开的所有窗口的句柄
print(all_handles)

#进入注册窗口
for handle in all_handles:
    if handle!=search_window:
        print("注册窗口的句柄为："+handle)
        driver.switch_to.window(handle)  #切换窗口
        driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_3__userName']").send_keys("lalla")
        driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_3__password']").send_keys("lalal")


#返回到搜索窗口
for handle in  all_handles:
    if handle==search_window:
        print("搜索窗口的句柄为："+handle)
        driver.switch_to.window(handle)
        driver.find_element_by_id("kw").send_keys("lxc")



