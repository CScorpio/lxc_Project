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
        self.find_element(By.XPATH,"//*[@title='2018年10月01日']").click()

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
        ele = self.find_element(By.XPATH,"HTML/BODY/DIV/DIV/DIV/DIV/DIV/SPAN/DIV/A/SPAN")  #这边会提示TypeError: rect is undefined
        #ele.click()
        ActionChains(self.driver).click(ele).perform()

    def click_ex_msg_btn(self):
        self.find_element(By.XPATH, "//tr[@data-recordindex='0']/td[3]/div/div/div/div/label[9]").click()

    def input_ex_msg_text(self,TA_code,clgm):
        #是否是证券类
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/span/div/fieldset[1]/div/span/div/div[1]/div/div/table[1]/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        self.find_element(By.XPATH,"/html/body/div[8]/div/ul/li[3]").click()

        #产品分类
        self.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div/span/div/fieldset[1]/div/span/div/div[1]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td/input").click()
        time.sleep(1)
        self.find_element(By.XPATH,"/html/body/div[9]/div/ul/li[2]").click()

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
        self.find_element(By.XPATH,"//*[@title='2018年10月01日']").click()

    def click_edit_btn(self):
        self.find_element(By.XPATH,"HTML/BODY/DIV/DIV/DIV/DIV/DIV/SPAN/DIV/A/SPAN").click()
''







