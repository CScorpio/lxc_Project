# coding=utf-8

from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver =  webdriver.Chrome()

driver.get("http://www.iqiyi.com/")
#driver.fullscreen_window()
driver.get_window_rect()
'''
元素的8种定位元素的方法：
find_element_by_id
find_element_by_name
find_element_by_class_name
find_element_by_tag_name
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_xpath
find_element_by_css_selector

还有一种By方式，需要导入from selenium.webdriver.common.by import By
find_element(By.8种方式)
'''

#driver.find_element_by_id("kw").send_keys("Selenium2")    #id定位元素
#driver.find_element_by_name("wd").send_keys("Selenium2")  #name定位元素
#driver.find_element_by_class_name("s_ipt").send_keys("Selenium2")  #class名称定位元素
#driver.find_element_by_tag_name("input").send_keys("Selenium2")  #tag定位元素

#driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/span/input").send_keys("Selenium2") #通过xpath的绝对路径定位元素
#driver.find_element_by_xpath("//input[@id='kw']").send_keys("Selenium2") #通过xpath的元素属性定位
#driver.find_element_by_xpath("//input[@class='s_ipt']").send_keys("Selenuim2")
#driver.find_element_by_xpath("//input[@name='wd']").send_keys("Selenium2")
#driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("Selenuim2")#通过层级和属性结合，来定位元素
#!!!!!!!!!!!!!!driver.find_element_by_xpath("//span[@class='bg s_ipt_wr quickdelete-wrap']/input").send_keys("Selenuim2") #有问题，这个找不到
#driver.find_element_by_xpath("//form[@id='form' and @name='f']/span/input").send_keys("Selenium2")  # 逻辑运算符and连接更多属性进行元素标识

#driver.find_element_by_css_selector(".s_ipt").send_keys("Selenium2")#通过css选择器class进行定位
#driver.find_element_by_css_selector("[id='kw']").send_keys("Selenuim2")#通过css选择器属性进行定位
#driver.find_element_by_css_selector("html>body>div>div>div>div>div>form>span>input").send_keys("李晓晨") #通过css选择器父子关系定位
#driver.find_element_by_css_selector("input#kw").send_keys("淘宝网")#通过css选择器id进行定位
#driver.find_element_by_css_selector("form#form>span>input#kw").send_keys("爱奇艺baidu") #css选择器的组合使用
#driver.find_element_by_css_selector("form.fm>span>input[name='wd']").send_keys("付宏旭") #css选择器的组合使用


#driver.find_element(By.ID,'kw').send_keys("http://192.168.1.101:7100/ifsp/login.html") #By定位元素的方法
#driver.find_element(By.NAME,'wd').send_keys("1")
#driver.find_element(By.CLASS_NAME,'s_ipt').send_keys("2")
#driver.find_element(By.TAG_NAME,"input").send_keys("3")
#driver.find_element(By.LINK_TEXT,'新闻').click()
#driver.find_element(By.PARTIAL_LINK_TEXT,'新').click()
#driver.find_element(By.XPATH,"//*[@id='form']/span/input[@autocomplete='off']").send_keys('4')
driver.find_element(By.CSS_SELECTOR,"form.fm>span>input[name='wd']").send_keys("5")



#driver.find_element_by_id("su").click()
#driver.find_element_by_link_text("地图").click() #link text定位元素
#driver.find_element_by_partial_link_text("地").click() #link text的部分字段定位元素

#driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/span[2]/input").click()  #通过xpath的绝对路径定位元素
#driver.find_element_by_xpath("//input[@id='su']").click()#通过xpath的元素属性定位  //表示当前目录下  input表示标签名 [@id='su']表示该标签下的属性id等于su
#driver.find_element_by_xpath("//*[@class='bg s_btn']").click() #如果标签名称不指定的情况下，可以用*代替，但是要求属性可以唯一标识一个元素
#driver.find_element_by_xpath("//span[@class='bg s_btn_wr']/input").click()

#driver.find_element_by_css_selector("#su").click()#通过css选择器id进行定位
driver.find_element_by_css_selector(".s_btn").click()  #class 名称为一个的时候可以找到，多个的时候找不到

#driver.quit()



