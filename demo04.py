import requests

url = 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=7d0c84a532de473faef69c73599f72b1&count=5&expiryDate=0&format=1&newLine=2'
res = requests.get(url).json()

iplist = list()
for i in res['msg']:
    ipport = i['ip']+':'+i['port']
    iplist.append(ipport)
print(iplist)


proxies = {
    'http':iplist[0]
}

response = requests.get('http://www.baidu.com',proxies=proxies)
print(response.content)
