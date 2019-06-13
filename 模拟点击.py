from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sahitest.com/demo/clicks.htm')

click_btn = driver.find_element_by_xpath('//input[@value="click me"]')
dbclick_btn = driver.find_element_by_xpath('//input[@value="dbl click me"]')
right_btn = driver.find_element_by_xpath('//input[@value="right click me"]')
ActionChains(driver).click(click_btn).double_click(dbclick_btn).context_click(right_btn).perform()
print(driver.find_element_by_name("t2").get_attribute("value"))
time.sleep(10)
driver.quit()