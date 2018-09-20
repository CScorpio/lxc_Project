from selenium import webdriver
import time
import logging

#logging.basicConfig(level=logging.DEBUG)  #捕捉客户端向服务端发送的post请求

driver=webdriver.Firefox()
driver.get("https://videojs.com/")


driver.implicitly_wait(10)
video=driver.find_element_by_xpath("html/body/section/div/video")
#video=driver.find_element_by_xpath("//video[@id='preview-player_html5_api']")
#video=driver.find_element_by_id("preview-player_html5_api")
#video=driver.find_element_by_css_selector("button.vjs-big-play-button")
#driver.get_screenshot_as_file("C:\\Users\\lixc\\Desktop\\webdriver\\ll.png")

#返回播放文件地址
url=driver.execute_script("return arguments[0].currentSrc;",video) #currentSrc 返回档期啊视频/音频的URL
print(url)

#播放视频
print("start")
driver.execute_script("return arguments[0].play();",video) #play()视频的播放
'''
为什么要这么写呢？
因为execute_script("")引号中只能是纯JS语句，但是video在python中获取到之后，在js中并没有这个参数。
所以需要将python中的video通过execute_script()方法，传到JS中，在JS语言中，进行video.play(),或者currentSrc，pause()等

'''

#播放15秒
time.sleep(15)

#暂停视频
print("stop")
driver.execute_script("arguments[0].pause()",video)  #pause视频的暂停

#driver.quit()

'''
arguments[] 和 return的使用方式


print(driver.execute_script("return 'this is first arg'+arguments[0]+'|'+' this is second arg'+arguments[1]; ",1,2))

print("=================")

print(driver.execute_script("'this is first arg'+arguments[0]+'|'+' this is second arg'+arguments[1]; ",1,2))
'''