from selenium import webdriver
import time
import os
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("upfile.html")
driver.get(file_path)

# #定位上传按钮，添加本地文件
# driver.find_element_by_xpath("//input[@name='file']").send_keys('C:\\Users\\lixc\\Desktop\\productdata.txt')

#单击打开上传窗口
#driver.find_element_by_xpath("//*[@type='file']").click()
fileBtn = driver.find_element_by_name("file")
print (fileBtn.size)
print (hasattr(fileBtn,"click")) #这个是用来查看这个对象里面有没有某个属性的方法 刚才写的dir是用来查看对象里面所有属性的方法
print(fileBtn.__dir__())
#fileBtn.click()
ActionChains(driver).click(fileBtn).perform()

os.system("D:\\cccccccchen\\webdriver\\upfile1.exe")
