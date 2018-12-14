from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.baidu.com/")
driver.get_screenshot_as_file("C:\\Users\\lixc\\Desktop\\lalaalalalallalalal.png")
print(driver.get_window_rect())
