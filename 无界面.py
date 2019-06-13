from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.set_headless()
driver =webdriver.Chrome(options=opt)

driver.get("http://www.baidu.com")
driver.save_screenshot('./a.png')