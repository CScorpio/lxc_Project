from selenium import webdriver
import os,time

driver=webdriver.Firefox()
file_path='file:///'+ os.path.abspath('checkbox.html')
driver.get(file_path)

'''
input_tag=driver.find_elements_by_tag_name("input")
for i in input_tag:
    if i.get_attribute('type')== 'checkbox':
        i.click()
        time.sleep(1)
    else:
        print(i.get_attribute('type'))
'''
#input_tag=driver.find_elements_by_xpath("//input[@type='checkbox']")
input_tag=driver.find_elements_by_css_selector("[type='checkbox']")
print(input_tag)

for i in input_tag:
    i.click()
    time.sleep(1)

print("type为checkbox的input_tag有"+str(len(input_tag))+"个")
print("type为checkbox的input_tag有",len(input_tag),"个")
driver.find_elements_by_css_selector("[type='checkbox']").pop(3).click() #pop()方法用于获取列表中的一个元素，默认为最后一个元素