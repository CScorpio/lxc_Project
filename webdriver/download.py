from selenium import webdriver
import time,os

#fp=webdriver.FirefoxProfile()

'''
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir",os.getcwd())
fp.set_preference("browser.helpApps.neverAsk.savaToDisk","application/octet-stream") #下载文件的类型
'''



driver = webdriver.Firefox()

driver.get("https://pc.weixin.qq.com/")

for i in range(10):
    print(i)
    time.sleep(1)
else:
    print("sleep end")

driver.stop_client()
#driver.find_element_by_partial_link_text("下载").click()
downloadBtn = driver.find_element_by_partial_link_text("下载")
print (downloadBtn.text)
print (downloadBtn.get_attribute("href"))
downloadBtn.click()