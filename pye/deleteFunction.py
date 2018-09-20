from selenium import webdriver
from pye.login_pye import LOGIN
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox();
driver.get("http://192.168.1.101:7100/ifsp/login.html")
driver.fullscreen_window()
LOGIN().login1(driver)

driver.find_element_by_xpath("//*[@id='moduleDisplay']/ul/li[3]").click()  #点击运营管理
sleep(1)
a=driver.find_element_by_xpath("//*[@id='treeview-1024-record-basicInfoMgtId']")  # 点击基础信息
ActionChains(driver).double_click(a).perform()
sleep(1)
driver.find_element_by_id("treeview-1024-record-agencyMgtId").click() #点击外部机构管理
sleep(1)
'''查看功能'''
driver.find_element_by_xpath("//tr[@data-recordindex='0']/td[3]/div/div/div/div/label[1]").click() #点击查看按钮
sleep(2)
driver.find_element_by_css_selector(".x-tool-img.x-tool-close").click() #查看后关闭

'''删除功能'''
driver.find_element_by_xpath("//tr[@data-recordindex='0']/td[3]/div/div/div/div/label[2]").click() #勾选第一条数据
sleep(1)
driver.find_element_by_xpath("HTML/BODY/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/A[2]/SPAN/SPAN/SPAN").click() #点击删除按钮
sleep(5)
driver.find_element_by_xpath("HTML/BODY/DIV/DIV/DIV/DIV/A[2]").click()  #确认是否删除，点击确定
sleep(1)
driver.find_element_by_css_selector(".x-tool-img.x-tool-close").click() #关闭删除成功的弹窗

'''查询功能'''
driver.find_element_by_name("agType").click() #点击查询字段：机构类型
sleep(1)
driver.find_element_by_xpath("HTML/BODY/DIV/DIV/ul/li[2]").click() #选择机构类型：私募基金管理公司

driver.find_element_by_name("agFullName").send_keys("外部机构") #在查询字段中输入机构名称：外部机构

sleep(2)

driver.find_element_by_css_selector(".x-btn.x-unselectable.x-box-item.x-btn-default-small.x-icon-text-left.x-btn-icon-text-left.x-btn-default-small-icon-text-left").click() #点击查询

