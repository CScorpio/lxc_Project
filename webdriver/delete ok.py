from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.get_screenshot_as_file("C:\\Users\\lixc\\Desktop\\webdriver\\lalaalalalallalalal.png")
print(driver.get_window_rect())
