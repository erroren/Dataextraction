from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/selectTest.htm')


s1 = Select(driver.find_element_by_id('s1Id'))
s1.select_by_index(1)
# print(s1.first_selected_option)

s1.select_by_value('o2')
# print(s1.first_selected_option.text)i
for i in s1.all_selected_options:
    print(i.text)