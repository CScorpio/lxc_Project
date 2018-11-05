from BasePage.PAGE.Page import BasePage
from BasePage.PAGE.LoginPage import Login
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  #显示等待
from selenium.webdriver.support import expected_conditions as EC  #设置等待执行语句


class test_Login(unittest.TestCase):

    def setUp(self):

        self.produce_code = '00326'
        self.TA_code = 'TAlxc'
        self.clgm = 50
        self.rbpz_name = 'rbpz1101'
        self.template_name = 'mb1101'
        self.element_code = '0010'
        self.send_days = '2'
        self.remark = 0

        self.url = 'http://192.168.1.101:7400/faext_s460/index.html'
        self.driver = webdriver.Firefox()
        self.loginpye = Login(self.driver, self.url)
        self.driver.maximize_window()

        
        print('test_Login测试开始')

    def tearDown(self):
        print('test_Login测试结束')


    def test_login(self):

        #点击登录
        self.loginpye.open(self.url)
        time.sleep(2)
        self.loginpye.input_username()
        self.loginpye.input_password()
        time.sleep(1)
        self.loginpye.click_submit()

        time.sleep(2)

        try:
            WebDriverWait(self.driver,30).until(
                EC.text_to_be_present_in_element(
                            (By.XPATH,"//span[@id='roleSelection-1018_header_hd-textEl']"),
                                             "角色选择1"))
            print("登录执行完成")
            self.remark += 1
        except BaseException:
            print("连接超时")

        if self.remark == 1:

            #选择角色
            self.loginpye.select_functionrole()
            self.loginpye.select_datarole()
            self.loginpye.click_confirm()

        else:
            print("登录执行失败，停止流程")
            return False


        a = self.driver.find_element(By.XPATH,"//*[@id='productInfo']/../label[3]").text

        try:
            WebDriverWait(self.driver,30).until(
                EC.text_to_be_present_in_element(
                    (By.XPATH,"/html/body/div[1]/div/div[2]/div/ul/li[1]"),
                            "首页"))
            print("角色选择执行完成，当前用户|功能-数据角色为：{}".format(a))
            self.remark += 1
        except BaseException:
            print("连接超时")

        if self.remark == 2:

            #选择菜单
            self.loginpye.Loading_Menues_yxgl()
            time.sleep(1)
            self.loginpye.Loading_Menues_product_management()
            time.sleep(1)
            self.loginpye.Loading_Menues_product()

        else:
            print("角色选择执行失败")
            return False

        # select_page_html = self.driver.page_source
        # print(select_page_html)
        #
        # return self.driver

        #新增
        self.loginpye.click_new_btn()
        time.sleep(2)
        #输入必填项
        self.loginpye.input_new_text(self.produce_code)

        #点击提交按钮
        self.loginpye.click_new_submit()

        time.sleep(2)
        #保存成功后点击确认按钮
        self.loginpye.click_save_success_confirm_btn()

        time.sleep(2)


        #点击扩展信息按钮
        self.loginpye.click_ex_msg_btn()

        #输入必填项
        self.loginpye.input_ex_msg_text(self.TA_code,self.clgm)

        #点击修改按钮
        self.loginpye.click_edit_btn()

        time.sleep(1)
        #点击修改成功按钮
        self.loginpye.click_edit_success_confirm_btn()

        time.sleep(2)
        #点击审核并且通过
        self.loginpye.click_Review_btn()
        time.sleep(2)
        self.loginpye.click_Review_pass_btn()
        time.sleep(1)
        self.loginpye.click_Review_success_confirm_btn()

        self.loginpye.click_close_Menues_btn()

        # 打开模板界面
        self.loginpye.Loading_Menues_xxpl()
        self.loginpye.Loading_Menues_mbxx_management()
        time.sleep(1)
        self.loginpye.Loading_Menues_mbwh()
        self.loginpye.click_mbwh_new_btn()
        time.sleep(2)
        self.loginpye.input_mbwh_text(self.template_name)
        self.loginpye.click_mbwh_new_submit()
        time.sleep(1)
        self.loginpye.click_mbwh_new_success_confirm_btn()

        # 点击选择披露元素按钮
        self.loginpye.click_xzplys_btn()

        # 选择0010开头的元素
        self.loginpye.select_plys(self.element_code)
        self.loginpye.click_add_0010_btn()

        self.element_code = '0002'
        # 选择0002开头的元素
        self.loginpye.select_plys(self.element_code)
        self.loginpye.click_add_0002_btn()

        # 点击关闭
        self.loginpye.click_close_plys_btn()

        self.loginpye.click_close_Menues_btn()

        #打开日报配置维护页面


        self.loginpye.Loading_Menues_rbpzwh()

        #点击新增配置按钮
        self.loginpye.click_xzpz_btn()

        time.sleep(2)
        #输入日报配置中的文本内容
        self.loginpye.input_rbpz_text(self.rbpz_name)

        #点击新增的提交按钮
        self.loginpye.click_rbpz_commit_btn()

        # ele = self.loginpye.get_alert_text()
        # alter_text =ele.text
        # print(alter_text)
        #
        # try:
        #      self.assertEqual(alter_text,"该日报配置已存在!",msg="日报配置已经存在，不需要再次配置")
        # except BaseException as msg:
        #     print(msg)
        # else:
        #     self.loginpye.click_confirm_btn()
        #     self.loginpye.click_close_btn()

        self.loginpye.click_confirm_btn()
        self.loginpye.click_close_Menues_btn()

        

        #打开产品报表元素设置界面
        self.loginpye.Loading_Menues_cpbb_manegement()
        time.sleep(1)
        self.loginpye.Loading_Menues_cpbbyssz()
        time.sleep(1)
        self.loginpye.click_cpbbys_new_btn()
        #输入产品报表元素设置界面的产品名称字段和报表配置字段
        self.loginpye.input_cpbbys_text_cp(self.produce_code)
        self.loginpye.click_cpxz_sumit_btn()

        self.loginpye.input_cpbbys_text_bb(self.rbpz_name)
        self.loginpye.click_cpxz_sumit_btn()
        #点击新增按钮
        self.loginpye.click_new_submit_btn()
        time.sleep(1)
        self.loginpye.click_mbwh_new_success_confirm_btn()

        self.loginpye.click_close_Menues_btn()

        #打开参数设置界面
        self.loginpye.Loading_Menues_xpcssz()
        time.sleep(1)
        self.loginpye.Loading_Menues_cpcssz()
        time.sleep(1)
        self.loginpye.click_new_cpcs_btn()
        self.loginpye.input_cpcs_text_cp(self.produce_code)
        self.loginpye.input_cpcs_text_scrq(self.send_days)
        self.loginpye.click_new_cpcs_submit_btn()
        self.loginpye.click_new_success_confirm_btn()

        self.loginpye.click_close_Menues_btn()

        #打开日报签名管理界面
        self.loginpye.Loading_Menues_bbqm_manegement()
        time.sleep(1)
        self.loginpye.Loading_Menues_rbqmgl()
        time.sleep(1)
        self.loginpye.click_create_btn()

        self.loginpye.input_create_text(self.produce_code)
        time.sleep(1)
        self.loginpye.click_creat_submit_btn()

        self.loginpye.click_creat_success_confirm_btn()

        
        











