from selenium import webdriver

driver = webdriver.Chrome()
url = 'http://tieba.baidu.com/f/search/res?qw=%E6%99%AF%E5%90%A7&sm=2&cf=1&ie=utf-8&red_tag=k3287472406'
driver.get(url)
# print(driver.page_source)
# dataList = driver.find_elements_by_css_selector("span.p_title")
# for data in dataList:
#     print(data.text)
driver.maximize_window()
dataList = driver.find_elements_by_xpath('//span[@class="p_title"]')
for data in dataList:
    print(data.id)
    print(data.text)
    print(data.location)
    print(data.tag_name)
    print(data.size)
# driver.quit()