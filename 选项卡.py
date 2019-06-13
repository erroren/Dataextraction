from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import  time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.execute_script('window.open()')
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
driver.get('http://taobao.com')
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
# driver.quit()