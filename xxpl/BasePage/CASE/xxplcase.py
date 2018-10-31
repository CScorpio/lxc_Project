from BasePage.PAGE.LoginPage import Login
from selenium import webdriver
import unittest
import time
import requests

class test_Login(unittest.TestCase):

    def setUp(self):
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

        #选择角色
        self.loginpye.select_functionrole()
        self.loginpye.select_datarole()
        self.loginpye.click_confirm()

        '''
        #选择菜单
        self.loginpye.Loading_Menues_yxgl()
        time.sleep(1)
        self.loginpye.Loading_Menues_product_management()
        time.sleep(1)
        self.loginpye.Loading_Menues_product()

        # select_page_html = self.driver.page_source
        # print(select_page_html)
        #
        # return self.driver

        #新增
        self.loginpye.click_new_btn()
        time.sleep(2)
        #输入必填项
        self.loginpye.input_new_text('00304')

        #点击提交按钮
        self.loginpye.click_new_submit()

        time.sleep(2)
        #保存成功后点击确认按钮
        self.loginpye.click_save_success_confirm_btn()

        time.sleep(2)


        #点击扩展信息按钮
        self.loginpye.click_ex_msg_btn()

        #输入必填项
        self.loginpye.input_ex_msg_text('TA',50)

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
        '''

        #打开日报配置维护页面
        self.loginpye.Loading_Menues_xxpl()
        # self.loginpye.Loading_Menues_mbxx_management()
        # time.sleep(1)
        # self.loginpye.Loading_Menues_rbpzwh()
        #
        # #点击新增配置按钮
        # self.loginpye.click_xzpz_btn()
        #
        # #输入日报配置中的文本内容
        # self.loginpye.input_rbpz_text('1017lxc')
        #
        # #点击新增的提交按钮
        # self.loginpye.click_rbpz_commit_btn()
        #
        # ele = self.loginpye.get_alert_text()
        # alter_text =ele.text
        # print(alter_text)
        #
        # try:
        #     self.assertEqual(alter_text,"该日报配置已存在!",msg="日报配置已经存在，不需要再次配置")
        # except BaseException as msg:
        #     print(msg)
        # else:
        #     self.loginpye.click_confirm_btn()
        #     self.loginpye.click_close_btn()

        # #打开模板界面
        # self.loginpye.Loading_Menues_mbwh()
        # self.loginpye.click_mbwh_new_btn()
        # time.sleep(2)
        # self.loginpye.input_mbwh_text('1017lxc')
        # self.loginpye.click_mbwh_new_submit()
        # time.sleep(1)
        # self.loginpye.click_mbwh_new_success_confirm_btn()
        #
        # #点击选择披露元素按钮
        # self.loginpye.click_xzplys_btn()
        #
        # #选择0010开头的元素
        # self.loginpye.select_plys('0010')
        # self.loginpye.click_add_0010_btn()
        #
        # #选择0002开头的元素
        # self.loginpye.select_plys('0002')
        # self.loginpye.click_add_0002_btn()
        #
        # #点击关闭
        # self.loginpye.click_close_plys_btn()

        # #打开产品报表元素设置界面
        # self.loginpye.Loading_Menues_cpbb_manegement()
        # time.sleep(1)
        # self.loginpye.Loading_Menues_cpbbyssz()
        # time.sleep(1)
        # self.loginpye.click_cpbbys_new_btn()
        # #输入产品报表元素设置界面的产品名称字段和报表配置字段
        # self.loginpye.input_cpbbys_text_cp('00318')
        # self.loginpye.click_cpxz_sumit_btn()
        #
        # self.loginpye.input_cpbbys_text_bb('1023rbpz')
        # self.loginpye.click_cpxz_sumit_btn()
        # #点击新增按钮
        # self.loginpye.click_new_submit_btn()
        # time.sleep(1)
        # self.loginpye.click_mbwh_new_success_confirm_btn()

        #打开日报签名管理界面
        self.loginpye.Loading_Menues_bbqm_manegement()
        time.sleep(1)
        self.loginpye.Loading_Menues_rbqmgl()
        time.sleep(1)
        self.loginpye.click_create_btn()



        











