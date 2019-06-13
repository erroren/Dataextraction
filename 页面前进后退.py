from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import  time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print(driver.title)
driver.find_element_by_link_text("新闻").click()
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[0])
print(driver.title)
time.sleep(2)
driver.find_element_by_link_text("体育").click()
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[0])
print(driver.title)
time.sleep(2)
# time.sleep(1)
# driver.back()
# time.sleep(1)
# driver.forward()
# print(driver.title)
driver.quit()