from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
try:
    element = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.ID, 'su'))
        EC.title_is('百度一下，你就知道')
    )
finally:
    driver.quit()