from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import  time

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
time.sleep(2)

dragMe = driver.find_element_by_xpath('//div[@class="drag"]')
item1 = driver.find_element_by_xpath("//div[contains(.,'Item 1')]")
item2 = driver.find_element_by_xpath("//div[contains(.,'Item 2')]")
item3 = driver.find_element_by_xpath("//div[contains(.,'Item 3')]")
item4 = driver.find_element_by_xpath("//div[contains(.,'Item 4')]")

ActionChains(driver).drag_and_drop(dragMe, item1).perform()
time.sleep(2)
ActionChains(driver).drag_and_drop_by_offset(dragMe, 130, 140).perform()
time.sleep(2)

driver.quit()
