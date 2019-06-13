from selenium import webdriver
from PIL import Image
from 验证码.超级鹰.chaojiying import Chaojiying_Client
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('https://kyfw.12306.cn/otn/login/init')
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(2)
driver.save_screenshot('./index.png')

image = driver.find_element_by_class_name('touclick-image')
username = driver.find_element_by_id('username')
passwd = driver.find_element_by_id('password')
submitbtn = driver.find_element_by_id('loginSub')
left = image.location['x']
top = image.location['y']
right = left+image.size['width']
bottom = top+image.size['height']
index = Image.open('./index.png')
image_crop = index.crop((left, top, right, bottom))
image_crop.save('./image.png')
chaojiying = Chaojiying_Client('982882262', '6623732', '899683')
image1 = open('./image.png', 'rb').read()
res = chaojiying.PostPic(image1, 9004)
print(res)
username.send_keys('18237416258')
passwd.send_keys('qq982882262')
clickOffsets = []
locations = res['pic_str'].split('|')
for location in locations:
    xy = location.split(',')
    x = int(xy[0])
    y = int(xy[1])
    ActionChains(driver).move_to_element_with_offset(image, x, y).click().perform()
    time.sleep(1)
submitbtn.click()
# driver.switch_to_window(driver.window_handles[1])
time.sleep(2)
# driver.quit()
