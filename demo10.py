import requests
import chardet
from bs4 import BeautifulSoup
from lxml import etree
# 蘑菇代理的隧道订单
appKey = "UXZrS3IyN1ZyNzhMWjlVSzpidnBMRHJIUkpTUFJpNjJC"

# 蘑菇隧道代理服务器地址
ip_port = 'transfer.mogumiao.com:9001'

# 准备去爬的 URL 链接
url = "https://tieba.baidu.com/f?kw=%E5%8A%A8%E6%BC%AB%E5%9B%BE%E7%89%87&ie=utf-8&tab=good&cid=0&pn=0"

proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    "Proxy-Authorization": 'Basic '+ appKey
}
r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
html = r.content.decode()
root = etree.HTML(html)
# res = root.xpath("//ul[@id='thread_list']/li//a[@class='thumbnail vpic_wrap']/img/@data-original")

res = root.xpath('//div[@class="t_con cleafix"]//a[@class="thumbnail vpic_wrap"]/img/@data-original')
# print(len(res))
for i in res:
    print(i)