from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://sahitest.com/demo/iframesTest.htm')
time.sleep(2)
print(driver.current_url)
frames = driver.find_elements_by_tag_name('iframe')
driver.switch_to.frame(frames[0])
print("++++++++++++")
print(driver.page_source)