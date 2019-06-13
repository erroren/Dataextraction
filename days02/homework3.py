import requests
from lxml import etree
appKey = "UXZrS3IyN1ZyNzhMWjlVSzpidnBMRHJIUkpTUFJpNjJC"
# 蘑菇隧道代理服务器地址
ip_port = 'transfer.mogumiao.com:9001'
url = 'https://www.qiushibaike.com/8hr/page/1/'
print(url)
proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    "Proxy-Authorization": 'Basic ' + appKey
}
response = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
html = response.content.decode()
print(html)
# root = etree.HTML(html)
