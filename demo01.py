from urllib import request
import chardet
url = 'http://www.baidu.com'
res = request.urlopen(url=url)
urlres = res.read().decode('utf-8')
print(res)
print(type(res))
print(urlres)
print(type(urlres))