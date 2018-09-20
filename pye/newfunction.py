from selenium  import webdriver
from pye.login_pye import LOGIN
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome();
driver.get("http://192.168.1.101:7100/ifsp/login.html")
LOGIN().login1(driver)
class NEWFUNCTION:

    def LoadingMenues(self):
        '''加载菜单'''
        driver.find_element_by_xpath("//*[@id='moduleDisplay']/ul/li[3]").click()  #点击运营管理
        sleep(1)
        a=driver.find_element_by_xpath("//*[@id='treeview-1024-record-basicInfoMgtId']")  # 点击基础信息
        ActionChains(driver).double_click(a).perform()
        sleep(1)
        driver.find_element_by_id("treeview-1024-record-userMgtId").click() #点击用户管理
        sleep(1)

    def NewFunciton(self):
        '''新增用户'''
        driver.find_element_by_xpath("//*[@id='button-1045-btnWrap']").click() #点击新增按钮
        sleep(1)

        '''输入新增信息'''
        driver.find_element_by_name("userCode").send_keys("gk4") #登录编码
        driver.find_element_by_xpath("//input[@class='x-form-field x-form-required-field x-form-text  ' and @name='userName']").send_keys("顾客4") #用户姓名


        driver.find_element_by_css_selector(".x-form-field.x-form-empty-field.x-form-required-field.x-form-text.x-trigger-noedit").click()#用户类型
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[6]/div/ul/li[3]").click() #选择用户类型为永久用户

        driver.find_element_by_css_selector(".x-trigger-index-0.x-form-trigger.x-form-search-trigger.x-form-trigger-first").click() #所属机构
        sleep(2)
        driver.find_element_by_css_selector(".x-form-field.x-form-radio.x-form-cb.singleRadio").click() #选择所属机构
        driver.find_element_by_css_selector(".x-btn.x-unselectable.x-box-item.x-toolbar-item.x-btn-default-small.x-noicon.x-btn-noicon.x-btn-default-small-noicon").click() #点击确认
        sleep(2)
        driver.find_element_by_css_selector(".x-btn.x-unselectable.x-btn-default-small.x-noicon.x-btn-noicon.x-btn-default-small-noicon").click() #点击新增按钮
        sleep(2)
        driver.find_element_by_css_selector(".x-btn.x-unselectable.x-box-item.x-toolbar-item.x-btn-default-small.x-noicon.x-btn-noicon.x-btn-default-small-noicon").click() #保存成功后点击确定按钮

        driver.find_element_by_xpath("HTML/BODY/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/TABLE/TBODY/TR/TD/DIV/DIV/DIV/DIV/LABEL").click() #点击编辑按钮


NEWFUNCTION().LoadingMenues()
NEWFUNCTION().NewFunciton()


'''
#driver.find_element_by_xpath("//input[@id='textfield-1297-inputEl']").send_keys("gk") #登录编码
#driver.find_element_by_css_selector(".x-form-field.x-form-required-field.x-form-text").send_keys("gk") #登录编码

#driver.find_element_by_xpath("//input[@id='textfield-1298-inputEl']").send_keys("顾客") #用户姓名
#driver.find_element_by_css_selector(".x-form-field.x-form-required-field.x-form-text").send_keys("顾客") #用户姓名
#driver.find_element_by_name("userName").send_keys("顾客") #用户姓名

#driver.find_element_by_id("dictComboBox-1302-inputEl").click() #用户类型
#driver.find_element_by_xpath("//input[@name='userType']").click() #用户类型

#driver.find_element_by_xpath("//*[@class='x-grid-row x-grid-data-row']/td/div").click() #选择所属机构
#driver.find_element_by_css_selector(".x-grid-row.x-grid-data-row").click() #选择所属机构
#aa=driver.find_element_by_css_selector(".x-grid-row.x-grid-data-row") #选择所属机构
#bb=driver.find_element_by_xpath("//tr[@data-recordindex='0']") #选择所属机构
#ActionChains(driver).move_to_element(bb).click().perform() #选择所属机构

#driver.find_element_by_xpath("//*[@class='x-btn-icon-el  ']").click() #点击确认

#driver.find_element_by_xpath("//*[@id='button-1312-btnIconEl']").click() #点击新增按钮
'''