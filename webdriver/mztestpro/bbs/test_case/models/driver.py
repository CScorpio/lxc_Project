from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器驱动
def browser():
    host = '127.0.0.1'
    dc = {'browserName':'chrome'}
    driver = webdriver.Remote(command_executor=host,
                              desired_capabilities=dc)
    return driver

if __name__ == '__main__':
    driver = browser()
    driver.get("https://www.baidu.com/")
    driver.quit()