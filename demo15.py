from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.zhihu.com/explore")
# print(browser.page_source)
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Buttom")')
# cookies = browser.get_cookies()
# for cookie in cookies:
#     print(cookie)

browser.maximize_window()
browser.save_screenshot('./a.png')
