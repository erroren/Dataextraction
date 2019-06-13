from selenium import webdriver
from PIL import Image
import pytesseract
import time


driver = webdriver.Chrome()
driver.get('http://my.cnki.net/elibregister/commonRegister.aspx')
driver.save_screenshot('./index.png')
img = driver.find_element_by_id('checkcode')
left = img.location['x']
top = img.location['y']
right = left+img.size['width']
bottom = top+img.size['height']
index = Image.open('./index.png')
img1 = index.crop((left, top, right, bottom))
img1.save('./img1.png')
checkimg = Image.open('./img1.png')
checkimg.show()
gray = checkimg.convert('L')
gray.show()
threshold = 155
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
bw = gray.point(table,'1')
bw.show()
codestr = pytesseract.image_to_string(bw)
print(codestr)

user = driver.find_element_by_id('username')
passwd = driver.find_element_by_id('txtPassword')
email = driver.find_element_by_id('txtEmail')
code = driver.find_element_by_id('txtOldCheckCode')
user.send_keys('18237416258@163.com')
passwd.send_keys('6623732..')
email.send_keys('18237416258@163.com')
code.send_keys(codestr)
btm = driver.find_element_by_id('ButtonRegister')
btm.click()