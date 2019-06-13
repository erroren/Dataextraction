from selenium import webdriver
import time
from PIL import Image
from 验证码.超级鹰.chaojiying import Chaojiying_Client
driver = webdriver.Chrome()
driver.get('https://www.ifeng.com/')
driver.find_element_by_xpath('//span[@class="login_in-1twGaNkr login_icon-WIExzV-k"]').click()
driver.switch_to.window(driver.current_window_handle)
frames = driver.find_element_by_xpath('//div[@class="box-1pZSPyeN"]/div/iframe')
x = frames.location['x']
y = frames.location['y']
driver.switch_to.frame(frames)
driver.find_element_by_xpath('//span[contains(@class,"vlognavid")]').click()
time.sleep(2)
username = driver.find_element_by_id('loginName')
pwd = driver.find_element_by_id('loginPwd')
codestr = driver.find_element_by_id('loginCode')
loginbtn = driver.find_element_by_id('loginbtn')
driver.save_screenshot('./login.png')
element = driver.find_element_by_xpath('//div[@id="codeImage"]/img')
print(element.location)
left = x+element.location['x']
top = y+element.location['y']
right = left+element.size['width']
bottom = top+element.size['height']
im = Image.open('./login.png')
im_crop = im.crop((left, top, right, bottom))
im_crop.save('./image.png')
chaojiying = Chaojiying_Client('982882262', '6623732', '899683')
image1 = open('./image.png', 'rb').read()
res = chaojiying.PostPic(image1, 5000)
username.send_keys('18237416258')
pwd.send_keys('Qq982882262')
codestr.send_keys(res['pic_str'])
loginbtn.click()

