import requests

# 蘑菇代理的隧道订单
appKey = "UEJWYVgzMUtLaHZXZnlUdTo3cUhtdUxOUkxMMzVDeDZk"

# 蘑菇隧道代理服务器地址
ip_port = 'transfer.mogumiao.com:9001'

# 准备去爬的 URL 链接
url = 'https://www.baidu.com/'

proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
headers = {"Proxy-Authorization": 'Basic ' + appKey}
r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
print(r.status_code)
print(r.content)
print(r.content.decode())
if r.status_code == 302 or r.status_code == 301 :
    loc = r.headers['Location']
    url_f = url + loc
    print(loc)
    r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    print(r.status_code)
    print(r.text)
    print(r.content.decode())
