from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get('https://tech.163.com/')
datalist = driver.find_elements_by_xpath('//div[@class="data_row news_article clearfix"]/div/div/h3/a')

for data in datalist:
    data.click()
    driver.switch_to.window(driver.window_handles[1])
    title = driver.find_element_by_xpath('//div[@class="post_content_main"]/h1').text
    print(title)
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # driver1 = webdriver.Chrome()
    # driver1.get(data.get_attribute('href'))
    # print(driver.title)
    # print("_______________________")
    # ActionChains(driver).click(data).perform()
    # print(driver.title)
    # content = driver.find_element_by_xpath('//div[@class="post_text"]')
    # print(content.text)
    # time.sleep(2)