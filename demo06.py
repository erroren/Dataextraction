from urllib import request
import requests
from lxml import etree

url = 'https://tieba.baidu.com/index.html'
response = requests.get(url)
res = response.content.decode()
root = etree.HTML(res)
res = root.xpath('//img[@src="https://tb1.bdstatic.com/tb/zhongguohua.jpg"]')
for i in res:
    # a = requests.get(res[i])
    # with open('./photo/{}.jpg'.format(str(i)), 'wb') as f:
    #     f.write(a.content)
    print(etree.tostring(i))


