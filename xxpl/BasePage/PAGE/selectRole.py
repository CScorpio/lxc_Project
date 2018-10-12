from BasePage.PAGE.Page import BasePage
from selenium.webdriver.common.by import By



class SelectRole(BasePage):

    def select_functionrole(self):
        self.find_element(By.XPATH,"//input[@id='combobox-1022-inputEl']").click()
        self.find_element(By.CSS_SELECTOR,"#boundlist-1026-listEl>ul>li").clic()

    def select_datarole(self):
        self.find_element(By.XPATH,"//input[@id='combobox-1023-inputEl']").click()
        self.find_element(By.CSS_SELECTOR,"#boundlist-1028-listEl>ul>li").click()

    def click_confirm(self):
        self.find_element(By.XPATH,"//*[@id='button-1025-btnWrap']").click()