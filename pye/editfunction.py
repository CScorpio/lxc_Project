from selenium import webdriver
from pye.login_pye import LOGIN
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome();
driver.get("http://192.168.1.101:7100/ifsp/login.html")
LOGIN().login1(driver)

driver.find_element_by_xpath("//*[@id='moduleDisplay']/ul/li[3]").click()  #点击运营管理
sleep(1)
a=driver.find_element_by_xpath("//*[@id='treeview-1024-record-basicInfoMgtId']")  # 点击基础信息
ActionChains(driver).double_click(a).perform()
sleep(1)
driver.find_element_by_id("treeview-1024-record-agencyMgtId").click() #点击外部机构管理
sleep(1)
driver.find_element_by_xpath("//tr[@data-recordindex='0']/td[3]/div/div/div/div/label[3]").click() #点击编辑按钮
sleep(1)
driver.find_element_by_name("agShortName").clear() #清空机构简称
sleep(1)
driver.find_element_by_name("agShortName").send_keys("lxc") #修改机构简称

driver.find_element_by_css_selector(".x-btn.x-unselectable.x-btn-default-small.x-noicon.x-btn-noicon.x-btn-default-small-noicon").click() #点击修改按钮
sleep(2)
driver.find_element_by_css_selector(".x-btn.x-unselectable.x-box-item.x-toolbar-item.x-btn-default-small.x-noicon.x-btn-noicon.x-btn-default-small-noicon").click()  # 保存成功后点击确定按钮



