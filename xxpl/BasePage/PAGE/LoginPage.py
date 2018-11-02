from BasePage.PAGE.Page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class Login(BasePage):
    '''
    登录页面
    '''

    def input_username(self):
        self.find_element(By.XPATH,"//input[@id='textfield-1012-inputEl']").send_keys('root')

    def input_password(self):
        self.find_element(By.XPATH,"//input[@id='textfield-1013-inputEl']").send_keys('111111')

    def click_submit(self):
        self.find_element(By.XPATH,"//span[@id='button-1015-btnWrap']").click()

    def select_functionrole(self):
        self.find_element(By.XPATH,"//input[@id='combobox-1022-inputEl']").click()
        self.find_element(By.CSS_SELECTOR,"#boundlist-1026-listEl>ul>li").click()

    def select_datarole(self):
        self.find_element(By.XPATH,"//input[@id='combobox-1023-inputEl']").click()
        self.find_element(By.CSS_SELECTOR,"#boundlist-1028-listEl>ul>li").click()

    def click_confirm(self):
        self.find_element(By.XPATH,"//*[@id='button-1025-btnWrap']").click()

    def Loading_Menues_yxgl(self):
        self.find_element(By.XPATH,"//*[@id='moduleDisplay']/ul/li[3]").click()

    def Loading_Menues_product_management(self):
        a = self.find_element(By.XPATH,"//*[@id='treeview-1024-record-productMgtId']")
        ActionChains(self.driver).double_click(a).perform()

        # self.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[2]/div[3]/div/table/tbody/tr[5]/td/div/img[2]").click()

    def Loading_Menues_product(self):
        self.find_element(By.XPATH,"//*[@id='treeview-1024-record-productPublishMgmtId']").click()

    def click_new_btn(self):
        self.find_element(By.XPATH,"//*[@id='button-1045-btnWrap']").click()

    def input_new_text(self,produce_code):
        self.find_element(By.XPATH,"//*[@name='productCode']").send_keys(produce_code) #产品代码
        self.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div/span/div/fieldset/div/span/div/div[2]/div/div/table[1]/tbody/tr/td[2]/input").send_keys(produce_code) #产品全称

        # 产品类型
        self.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div/span/div/fieldset/div/span/div/div[3]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        self.find_element(By.XPATH,"//*[@class='x-list-plain']/li[30]").click()

        #管理人
        self.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div/span/div/fieldset/div/span/div/div[4]/div/div/table[1]/tbody/tr/td[2]/table/tbody/tr/td[2]").click()
        time.sleep(1)
        ele = self.find_element(By.XPATH,"//*[@data-recordid='b2d691b116384d57b48c7e43d9a4cfed']")
        ActionChains(self.driver).click(ele).perform()

        self.find_element(By.XPATH, "HTML/BODY/DIV/DIV/DIV/DIV/A/SPAN").click()

        #托管人
        self.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div/span/div/fieldset/div/span/div/div[4]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]").click()
        time.sleep(1)
        ele = self.find_element(By.XPATH,"//*[@data-recordid='b945cd9176f14f46a3ef3103fa4fd95f']")
        ActionChains(self.driver).click(ele).perform()
        self.find_element(By.XPATH,"HTML/BODY/DIV/DIV/DIV/DIV/A/SPAN").click()

        #合同成立日
        self.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div/span/div/fieldset/div/span/div/div[6]/div/div/table[1]/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        self.find_element(By.XPATH,"//*[@title='2018年10月31日']").click()

        #合同到期日
        self.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div/span/div/fieldset/div/span/div/div[6]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        self.find_element(By.XPATH, "/html/body/div[9]/div/table/tbody/tr[5]/td[4]").click()

    def click_new_submit(self):
        self.find_element(By.XPATH,"HTML/BODY/DIV/DIV/DIV/DIV/DIV/SPAN/DIV/A/SPAN").click()

    def click_save_success_confirm_btn(self):
        self.find_element(By.CSS_SELECTOR,".x-btn.x-unselectable.x-box-item.x-toolbar-item.x-btn-default-small.x-noicon.x-btn-noicon.x-btn-default-small-noicon").click()

    def click_Review_btn(self):
        self.find_element(By.XPATH,"//tr[@data-recordindex='0']/td[3]/div/div/div/div/label[7]").click()

    def click_Review_pass_btn(self):
        ele = self.find_element(By.XPATH,"HTML/BODY/DIV/DIV/DIV/DIV/DIV[3]/SPAN/DIV/A")
        print(ele.is_displayed())
        ele.click()

    def click_Review_success_confirm_btn(self):
        self.find_element(By.XPATH,"HTML/BODY/DIV/DIV/DIV/DIV/A/SPAN").click()


    def click_ex_msg_btn(self):
        self.find_element(By.XPATH, "//tr[@data-recordindex='0']/td[3]/div/div/div/div/label[9]").click()

    def input_ex_msg_text(self,TA_code,clgm):
        #是否是证券类
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/span/div/fieldset[1]/div/span/div/div[1]/div/div/table[1]/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        self.find_element(By.XPATH,"/html/body/div[8]/div/ul/li[3]").click()

        #产品分类
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/span/div/fieldset[1]/div/span/div/div[1]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        time.sleep(1)
        self.find_element(By.XPATH,"/html/body/div[9]/div/ul/li[3]").click()

        #TA代码
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/span/div/fieldset[1]/div/span/div/div[4]/div/div/table[1]/tbody/tr/td[2]/input").send_keys(TA_code)

        #成立规模
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/span/div/fieldset[1]/div/span/div/div[2]/div/div/table[2]/tbody/tr/td[2]/input").send_keys(clgm)

        #是否分级分类
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/span/div/fieldset[3]/div/span/div/div[2]/div/div/table[1]/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        time.sleep(1)
        self.find_element(By.XPATH,"/html/body/div[10]/div/ul/li[2]").click()



        #合同生效日
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/span/div/fieldset[3]/div/span/div/div[1]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        self.find_element(By.XPATH,"//*[@title='2018年10月31日']").click()

    def click_edit_btn(self):
        self.find_element(By.XPATH,"HTML/BODY/DIV/DIV/DIV/DIV/DIV/SPAN/DIV/A/SPAN").click()

    def click_edit_success_confirm_btn(self):
        self.find_element(By.XPATH,"HTML/BODY/DIV/DIV/DIV/DIV/A").click()


    #日报配置维护页面
    def Loading_Menues_xxpl(self):
        self.find_element(By.XPATH, "//*[@id='moduleDisplay']/ul/li[7]").click()

    def Loading_Menues_mbxx_management(self):
        a = self.find_element(By.XPATH, "//*[@id='treeview-1024-record-templateInfoMgtId']")
        ActionChains(self.driver).double_click(a).perform()

    def Loading_Menues_rbpzwh(self):
        self.find_element(By.XPATH,"//*[@id='treeview-1024-record-dayReportConfMgtId']").click()

    def click_xzpz_btn(self):
        self.find_element(By.XPATH,"//span[text()='新增']").click()

    def input_rbpz_text(self,rbpz_name):
        #报表配置名称
        self.find_element(By.XPATH,"//label[text()='报表配置名称:']/../../td[2]/input").send_keys(rbpz_name)
        #"/html/body/div[4]/div[2]/div/div/div/div/div/div/div/table[1]/tbody/tr/td[2]/input"
        #产品分类
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/div/div/div[1]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td").click()
        self.find_element(By.XPATH,"//li[text()='普通型']").click()
        #"/html/body/div[6]/div/ul/li[2]"
        #运作方式
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/div/div/div[2]/div/div/table[1]/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        self.find_element(By.XPATH,"//li[text()='开放式']").click()

        #时间属性
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/div/div/div[2]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        self.find_element(By.XPATH,"//li[text()='上市前']").click()

        #频度属性
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/div/div/div[3]/div/div/table[1]/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        self.find_element(By.XPATH,"//li[text()='最后一日']").click()

        #模板
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/div/div/div[3]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        self.find_element(By.XPATH,"//li[text()='mb1101']").click()

        #是否分级分类
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/div/div/div[4]/div/div/table[1]/tbody/tr/td[2]/div/table/tbody/tr/td[2]/table/tbody/tr/td/input").click()

    def click_rbpz_commit_btn(self):
        self.find_element(By.XPATH,"HTML/BODY/DIV/DIV/DIV/DIV/DIV/SPAN/DIV/A").click()

    def get_alert_text(self):
        ele = self.find_element(By.XPATH,"/html/body/div[12]/div[2]/div/div/div[1]/div/div/div[2]/span/div/table[1]/tbody/tr/td[2]/div")
        return ele

    def click_confirm_btn(self):
        self.find_element(By.XPATH,"HTML/BODY/DIV/DIV/DIV/DIV/A").click()

    def click_close_btn(self):
        self.find_element(By.XPATH,"HTML/BODY/DIV[4]/DIV/DIV/DIV/DIV/DIV[2]").click()

    #模板维护界面
    def Loading_Menues_mbwh(self):
        self.find_element(By.XPATH,"//*[@id='treeview-1024-record-templateMgtId']").click()

    def click_mbwh_new_btn(self):
        self.find_element(By.XPATH,"HTML/BODY/DIV/DIV/DIV[3]/DIV/DIV[4]/DIV/DIV[2]/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/DIV/A/SPAN").click()

    def input_mbwh_text(self,template_name):
        #模板名称
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/span/div/fieldset/div/span/div/div[1]/div/div/table/tbody/tr/td[2]/input").send_keys(template_name)

        #模板类型
        #//*[@id="boundlist-1136-listEl"]/ul
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/span/div/fieldset/div/span/div/div[2]/div/div/table/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        self.find_element(By.XPATH,"//li[text()='临时公告']").click()

    def click_mbwh_new_submit(self):
        self.find_element(By.XPATH,"HTML/BODY/DIV[7]/DIV[3]/DIV/DIV/DIV/SPAN/DIV/A").click()

    def click_mbwh_new_success_confirm_btn(self):
        self.find_element(By.XPATH,"HTML/BODY/DIV/DIV/DIV/DIV/A").click()

    #选择披露元素
    def click_xzplys_btn(self):
        xzplys_btn = self.find_element(By.XPATH,"//label[text()='选择披露元素']").click()
        ActionChains(self.driver).click(xzplys_btn).perform()

    def select_plys(self,element_code):
        ele = self.find_element(By.XPATH,"//label[text()='元素编号:']/../../td[2]/input")
        ele.send_keys(element_code)
        self.find_element(By.XPATH,"//label[text()='元素编号:']/../../../../../a").click()
        ele.clear()

    def click_add_0010_btn(self):
        self.find_element(By.XPATH,"//*[@data-recordid='c7f5eb04238947dabcbc229da55e15bd']/td[3]/div/div/div/div/label").click()

    def click_add_0002_btn(self):
        self.find_element(By.XPATH,"//*[@data-recordid='4c6228a3572d457da96239fb0c2d8a67']/td[3]/div/div/div/div/label").click()

    def click_close_plys_btn(self):
        self.find_element(By.XPATH,"//span[text()='关闭']/..").click()

    #产品报表元素设置界面
    def Loading_Menues_cpbb_manegement(self):
        cpbbgl_ele = self.find_element(By.XPATH, "//*[@id='treeview-1024-record-productReportMgtId']")
        ActionChains(self.driver).double_click(cpbbgl_ele).perform()

    def Loading_Menues_cpbbyssz(self):
        self.find_element(By.XPATH,"//*[@id='treeview-1024-record-productReportElementConfId']").click()

    def click_cpbbys_new_btn(self):
        self.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div[4]/div/div[2]/div/div/div/div/div/div/div/div/div/a/span/span").click()

    def input_cpbbys_text_cp(self,product_code):
        #点击产品名称的放大镜按钮
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/span/div/fieldset/div/span/div/div[1]/div/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]").click()
        #输入产品套账号
        self.find_element(By.XPATH,"/html/body/div[8]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/table[1]/tbody/tr/td[2]/input").send_keys(product_code)
        #点击套账号查询
        self.find_element(By.XPATH,"/html/body/div[8]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/a").click()
        #点击添加按钮
        self.find_element(By.XPATH,"html/body/div[8]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr/td[3]/div/div/div/div/label").click()

    def input_cpbbys_text_bb(self,rbpz_name):
        #点击报表配置名称的放大镜按钮
        self.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/span/div/fieldset/div/span/div/div[2]/div/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]").click()
        #输入报表配置名称
        self.find_element(By.XPATH,"/html/body/div[8]/div[2]/div/div/div/div/div[1]/div/div/table/tbody/tr/td[2]/input").send_keys(rbpz_name)
        time.sleep(1)
        #点击报表配置名称查询
        self.find_element(By.XPATH,"/html/body/div[8]/div[2]/div/div/div/div/div[1]/div/div/a/span/span").click()
        time.sleep(1)
        #点击数据
        self.find_element(By.XPATH,"/html/body/div[8]/div[2]/div/div/div/div/div[2]/div[2]/div/table/tbody/tr/td").click()


    def click_cpxz_sumit_btn(self):
        #点击确认按钮
        self.find_element(By.XPATH,"//span[text()='确认']/..").click()

    def click_new_submit_btn(self):
        self.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div/div/span/div/a").click()

    def click_cpbbyssz_new_success_confirm_btn(self):
        self.find_element(By.XPATH,"HTML/BODY/DIV/DIV/DIV/DIV/A").click()

    #日报签名管理界面
    def Loading_Menues_bbqm_manegement(self):
        bbqmgl_ele = self.find_element(By.XPATH, "//*[@id='treeview-1024-record-reportSignMgtId']")
        ActionChains(self.driver).double_click(bbqmgl_ele).perform()

    def Loading_Menues_rbqmgl(self):
        self.find_element(By.XPATH,"//*[@id='treeview-1024-record-dayReportResultMgtId']").click()

    def click_create_btn(self):
        self.find_element(By.XPATH,"//span[text()='创建']/..").click()

    def input_create_text(self,product_code):
        #选择日报日期
        self.find_element(By.XPATH,"//label[text()='日报日期:']/../../td[2]/table/tbody/tr/td/input").click()
        self.find_element(By.XPATH,"//td[@title='今天']").click()

        #选择产品名称
        self.find_element(By.XPATH,"//*[@name='productName']/../../td[2]").click()

        self.find_element(By.XPATH,"//*[@name='assetCode']").send_keys(product_code)
        search_ele = self.find_element(By.XPATH,"//*[@name='assetCode']/../../../../../a/span")
        #"/html/body/div[9]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/a/span"
        ActionChains(self.driver).double_click(search_ele).perform()
        time.sleep(1)
        self.find_element(By.XPATH,"//label[text()='添加']").click()
        self.find_element(By.XPATH,"//span[text()='确认']/..").click()

    def click_creat_submit_btn(self):
        self.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div/div/span/div/a/span").click()

    #这是一个点击关闭按钮
    def click_close_Menues_btn(self):
        self.find_element(By.XPATH,"//span[@class='x-tab-close-btn']").click()

    #在产品参数设置中设置送出日期
    def Loading_Menues_xpcssz(self):
        cpbbgl_ele = self.find_element(By.XPATH, "//*[@id='treeview-1024-record-xbrlParamerterMgtId']")
        ActionChains(self.driver).double_click(cpbbgl_ele).perform()

    def Loading_Menues_cpcssz(self):
        self.find_element(By.XPATH,"//*[@id='treeview-1024-record-productParamMgtId']").click()

    def click_new_cpcs_btn(self):
        self.find_element(By.XPATH,"//span[text()='新增']").click()

    def input_cpcs_text_cp(self,product_code):
        self.find_element(By.XPATH,"//div[@class = 'x-trigger-index-0 x-form-trigger x-form-search-trigger x-form-trigger-first']").click()
        self.find_element(By.XPATH,"//label[text()='产品套账号:']/../../td[2]/input").send_keys(product_code)

        self.find_element(By.XPATH,"//label[text()='产品套账号:']/../../../../../a").click()
        self.find_element(By.XPATH,"//label[text()='添加']").click()
        self.find_element(By.XPATH,"/html/body/div[8]/div[3]/div/div/a").click()

    def input_cpcs_text_scrq(self,send_days):
        self.find_element(By.XPATH, "//label[text()='日报送出日期:']/../../td[2]/input").send_keys(send_days)

    def click_new_cpcs_submit_btn(self):
        self.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div/div/span/div/a/span").click()

    def click_new_success_confirm_btn(self):
        self.find_element(By.XPATH,"html/body/div[5]/div[3]/div/div/a/span").click()




                                   





    








