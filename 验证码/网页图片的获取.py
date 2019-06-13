from selenium import webdriver
from PIL import Image

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.maximize_window()
browser.save_screenshot('./baidu.png')
element = browser.find_element_by_xpath('//div[@id="lg"]/img[1]')
print(element.location)
left = element.location['x']
top = element.location['y']
right = left+element.size['width']
bottom = top+element.size['height']
# print(left)

im = Image.open('./baidu.png')
im_crop = im.crop((left, top, right, bottom))
im_crop.save('./image.png')
browser.quit()