from selenium.webdriver.common.by import By

class Base_Page(object):
    '''
    1.抽方法
    1.1 driver = webderiver.fox() chrome()
    1.2 driver.get(url)
    1.3 element = driver.findelement
    1.4 element.operation(getvalue,click,sendkeys)
    1.5 driver.quit()
    '''


    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def openPage(self):
        self.driver.get(self.url)

    def findElement(self,type,value):
        return self.driver.find_element(type,value)

    def click(self,element):
        element.click()

    def getValue(self,element):
        return element.text

    def sendKeys(self,element,value):
        element.send_keys(value)

    def switchframe(self,value):
        self.driver.switch_to.frame(value)

    def quit(self):
        self.driver.quit()
