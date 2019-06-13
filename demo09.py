import requests
import chardet
from bs4 import BeautifulSoup
# 蘑菇代理的隧道订单
appKey = "UXZrS3IyN1ZyNzhMWjlVSzpidnBMRHJIUkpTUFJpNjJC"

# 蘑菇隧道代理服务器地址
ip_port = 'transfer.mogumiao.com:9001'

# 准备去爬的 URL 链接
url = "https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    "Proxy-Authorization": 'Basic '+ appKey
}
r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
if r.status_code == 302 or r.status_code == 301:
    loc = r.headers['Location']
    url_f = "https://ip.cn" + loc
    print(loc)
    r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    print(r.status_code)
    print(r.text)
print(chardet.detect(r.content)['encoding'])
html = r.content.decode(chardet.detect(r.content)['encoding'])
soup = BeautifulSoup(html, 'lxml')
res = soup.select('div[class="dw_table"]>div[class="el"]')
print(len(res))
for i in res:
    jobname = i.select("p>span>a")[0]['title']
    company = i.select("span[class='t2']>a")[0]['title']
    workplace = i.select("span[class='t3']")[0].get_text()
    salary = i.select("span[class='t4']")[0].get_text()
    pubtime = i.select("span[class='t5']")[0].get_text()
    print(jobname,company,workplace,salary,pubtime)