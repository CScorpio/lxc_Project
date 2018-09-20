from selenium.webdriver import Remote


#定义主机以及浏览器  不是，这个就是个参数
lists = {'http://127.0.0.1:4444/wd/hub':'chrome',
         'http://127.0.0.1:5555/wd/hub':'firefox',
         'http://127.0.0.1:5556/wd/hub':'internet explorer'

}

#通过不同的浏览器执行脚本
for host,browser in lists.items():
    print(host,browser)
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform':'ANY',
                                          'browserName': browser,
                                          'version': '',
                                          'javascriptEnabled': True,
                                          }
    )
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(browser)
    driver.find_element_by_id("su").click()





'''

#调用remote方法
driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities={'platform':'ANY',
                                      'browserName':'firefox',
                                      'version':'',
                                      'javascriptEnabled':True
                                      }
)

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("lalala")
driver.find_element_by_id("su").click()





#driver.close()

'''