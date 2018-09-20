from selenium import webdriver
import time
import logging


class LOGIN:
    def login1(self,driver):
        driver.find_element_by_xpath("//input[@id='textfield-1012-inputEl']").send_keys("root")
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='textfield-1013-inputEl']").send_keys("111111")
        time.sleep(1)
        driver.find_element_by_xpath("//span[@id='button-1015-btnWrap']").click()

        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='combobox-1022-inputEl']").click()
        driver.find_element_by_css_selector("#boundlist-1026-listEl>ul>li").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='combobox-1023-inputEl']").click()
        driver.find_element_by_css_selector("#boundlist-1028-listEl>ul>li").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='button-1025-btnWrap']").click()

    def logout1(self,driver):
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='button-1020-btnInnerEl']").click()




