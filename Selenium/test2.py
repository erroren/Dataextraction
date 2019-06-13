from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://tech.163.com/") # requests.get()

# for i in range(3):
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#     time.sleep(2)

# root.xpath("路径表达式")

print(driver.page_source)

newsList = driver.find_elements_by_xpath("//div[@class='data_row news_article clearfix']")
print(len(newsList))
for news in newsList:
    title = news.find_element_by_xpath("./div/div/h3/a")
    if title.get_attribute('href').find('tech.163.com') == -1:


