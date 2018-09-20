# coding=utf-8
from selenium import webdriver
import os
"""
截图函数
"""


#截图函数:为了保持项目的可移植性，
def insert_img(driver,file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))  #os.path.dirname(__file__)获取当前文件的路径，及获取了当前路径的上一次路径
                                                           #当前文件的路径：D:/Project_lxc/webdriver/mztestpro/bbs/test_case
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/') #D:/Project_lxc/webdriver/mztestpro/bbs/test_case
    base = base_dir.split('/test_case')[0] #D:/Project_lxc/webdriver/mztestpro/bbs
    file_path = base + "/report/image/" + file_name  #D:/Project_lxc/webdriver/mztestpro/bbs/report/image/baidu.png
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    insert_img(driver,'baidu.png')
    driver.quit()

