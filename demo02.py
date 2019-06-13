from urllib import request

proxy = {'http': '113.108.242.36:47713'}
proxyhandler = request.ProxyHandler(proxy)
opener = request.build_opener(proxyhandler)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')]
request.install_opener(opener)
url = 'http://ip.27399.com/'
# url = 'http://www.baidu.com'
res = request.urlopen(url)
html = res.read().decode('utf-8')
print(html)