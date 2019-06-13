import re
import requests


response = requests.get('https://www.qiushibaike.com/')
html = response.content.decode()
res = re.findall('<li class="item typs.*?".*?>(.*?)</li>', html, re.M | re.S)
for index in res:
    title = re.findall('<a class="recmd-content".*?>(.*?)</a>', index, re.M | re.S)
    messages = re.findall('<div class="recmd-num">(.*?)</div>', index, re.M | re.S)
    message = re.findall('<span>(.*?)</span>', messages[0], re.M | re.S)
    author = re.findall('<span class="recmd-name">(.*?)</span>', index, re.M | re.S)
    print(title[0], message[0], message[3], author[0])
