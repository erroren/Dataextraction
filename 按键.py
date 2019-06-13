from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sahitest.com/demo/keypress.htm')


KeyUp = driver.find_element_by_id('r1')
KeyDown = driver.find_element_by_id('r2')
KeyPress = driver.find_element_by_id('r3')

result = driver.find_element_by_name('t1')
enter = driver.find_element_by_name('t2')

KeyUp.click()
ActionChains(driver).key_down('a',enter).key_up('a').perform()
print(result.get_attribute('value'))
enter.clear()
time.sleep(2)
KeyPress.click()
# ActionChains(driver).send_keys('b').perform()
ActionChains(driver).key_down('b',enter).key_up('b').perform()
print(result.get_attribute('value'))

