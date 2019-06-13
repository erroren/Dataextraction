import requests
from lxml import etree
import time

for i in range(1, 6):
    # 蘑菇代理的隧道订单
    appKey = "UEJWYVgzMUtLaHZXZnlUdTo3cUhtdUxOUkxMMzVDeDZk"

    # 蘑菇隧道代理服务器地址
    ip_port = 'transfer.mogumiao.com:9001'
    url = 'https://www.xicidaili.com/nn/'+str(i)
    print(url)
    proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        "Proxy-Authorization": 'Basic ' + appKey
    }
    response = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    html = response.content.decode()
    root = etree.HTML(html)
    IP = root.xpath('//table[@id="ip_list"]//tr/td[2]/text()')
    PORT = root.xpath('//table[@id="ip_list"]//tr/td[3]/text()')
    TYPE = root.xpath('//table[@id="ip_list"]//tr/td[6]/text()')
    for j in range(len(IP)):
        str1 = "IP:"+IP[j]+"PORT:"+PORT[j]+"TYPE:"+TYPE[j]+"\n"
        with open('./dirone/第{}页.txt'.format(str(i)), 'a', encoding='utf-8') as f:
            f.write(str1)
    time.sleep(1)