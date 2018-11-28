from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")

#显示等待：使webdriver等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）

'''
WebDriverWait类是由webDriver提供的等待方法，在设置时间内，默认隔一段时间监测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常
WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exception=None)
driver:浏览器驱动
timeout：最长超时时间，默认以秒为单位
poll_frequency=0.5：检测的间隔（步长）时间，默认为0.5s
ignored_exception:超时后的异常信息，默认情况下抛NoSuchElementException异常

WebDriverWait一般配合until()或者until_not()使用
until：调用该方法提供的驱动程序作为一个参数，直到返回值为True
until_not:调用该方法提供的驱动程序作为一个参数，直到返回值为false
'''


''''''

try:
    print(time.ctime())
    element=WebDriverWait(driver,10,0.5,NoSuchElementException).until(expected_conditions.presence_of_element_located((By.ID,"k")))
    element.send_keys("selenium")
except TimeoutException as msg:
    print(msg)
finally:
    print(time.ctime())

'''
print(time.ctime())
for i in range(10):
    print(i)
    try:
        e1=driver.find_element_by_id("kw22")
        if e1.is_displayed():
            print("is displayed")
            break
    except:pass
    time.sleep(1)
else:
    print("time out")
driver.close()
print(time.ctime())
'''

# #隐式等待：通过一定的时长等待页面上某元素加载完成，如果超出了设置的时长元素还没有被加载完成，则抛出NoSuchElementException异常
#
# driver.implicitly_wait(10)
# driver.get("https://www.baidu.com/")
#
# try:
#     print(time.ctime())
#     driver.find_element_by_id("k").send_keys("selenium")
#     driver.find_element_by_id("s").click()
# except NoSuchElementException as a:
#     print(a)
# finally:
#     print(time.ctime())









