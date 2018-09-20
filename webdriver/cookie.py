from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("http://youdao.com")


driver.add_cookie({'name':'lxc','value':'lxc11','haha':'////'})  #？？addcookie中字典对象应该可以有多个呀，为什么其他的键值对进不去呢？？？

cookies=driver.get_cookies()
print(cookies)

for cookie in cookies:
    print(cookie['name']+'--->'+cookie['value']+'--->'+cookie['path'])

#driver.delete_all_cookies() #删除所有cookie
driver.delete_cookie('lxc')   #删除name=lxc的cookie
cookies1=driver.get_cookie('lxc')  #获取name=lxc的cookie
print(cookies1)


'''
cookies1=driver.get_cookies()  #获取所有cookies
print(cookies1)     
'''

'''
cookies1=driver.get_cookies()
for i in cookies1:
    print(i['name']+'**'+i['path'])   
'''
'''
cookies1=driver.get_cookies()
for cookie in cookies1:
    print(cookie['name']+'--->'+cookie['value'])
'''