from selenium.webdriver.common.by import By
testcuple = (By.ID,"xxx")

print(testcuple)
print("=============")
#xxx = *testcuple #扎心了
print(*testcuple)

print(type(*testcuple))#我们来看一下使用*以后，这个返回的时个什么类型的