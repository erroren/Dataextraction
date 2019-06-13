
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sahitest.com/demo/mouseover.htm')

write = driver.find_element_by_xpath('//input[@value="Write on hover"]')
blank = driver.find_element_by_xpath('//input[@value="Blank on hover"]')

result = driver.find_element_by_name('t1')
action = ActionChains(driver)
action.move_to_element(write).perform()
print(result.get_attribute('value'))
time.sleep(2)

action.move_by_offset(10, 50).perform()
print(result.get_attribute('value'))
time.sleep(2)


action.move_to_element_with_offset(blank, 10, -40).perform()
print(result.get_attribute('value'))
time.sleep(2)
driver.quit()

