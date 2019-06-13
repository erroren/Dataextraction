from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import  time

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/alertTest.htm')
time.sleep(2)
driver.find_element_by_xpath('//input[@name="b1"]').click()
time.sleep(1)
a1 = driver.switch_to_alert()
time.sleep(1)
a1.accept()
time.sleep(1)
driver.quit()