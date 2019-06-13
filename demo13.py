from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# brower = webdriver.Chrome()
# brower.get('http://fanyi.baidu.com/')
driver = webdriver.PhantomJS()
time.sleep(1)
driver.get('http://www.baidu.com/')
data = driver.find_element_by_id("wrapper").text
# print(data)
# print(driver.title)
# driver.save_screenshot('./百度一下,你就知道.jpg')
driver.find_element_by_id('kw').send_keys("河南大学")
driver.find_element_by_id('su').click()
time.sleep(1)
driver.save_screenshot('./河南大学.png')