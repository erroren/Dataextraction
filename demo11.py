import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
agent = UserAgent()
print(agent.data)
for i in range(10):
    print(agent.random)
# # 蘑菇代理的隧道订单
# appKey = "UXZrS3IyN1ZyNzhMWjlVSzpidnBMRHJIUkpTUFJpNjJC"
#
# # 蘑菇隧道代理服务器地址
# ip_port = 'transfer.mogumiao.com:9001'
#
# # 准备去爬的 URL 链接
# url = 'http://zst.aicai.com/ssq/openInfo/'
#
# proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
#     "Proxy-Authorization": 'Basic ' + appKey
# }
# r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
# print(r.status_code)
# print(r.content)
# if r.status_code == 302 or r.status_code == 301:
#     loc = r.headers['Location']
#     url_f = "https://ip.cn" + loc
#     print(loc)
#     r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
#     print(r.status_code)
#     print(r.text)
# html = r.content.decode()
# soup = BeautifulSoup(html, 'lxml')
# res = soup.select('table[class="fzTab nbt"]>tbody>tr')
# print(len(res))
# for i in range(2,len(res)):
#     num = res[i].select('td')[0].get_text()
#     data = res[i].select('td')[1].get_text()
#     red =''
#     for nu in range(2,8):
#         red = red +' '+ res[i].select('td')[nu].get_text()
#     blue = res[i].select('td')[8].get_text()
#     money = res[i].select('td')[9].get_text()
#     firstnum = res[i].select('td')[10].get_text()
#     firstmoney = res[i].select('td')[11].get_text()
#     secnum = res[i].select('td')[12].get_text()
#     secmoney = res[i].select('td')[13].get_text()
#     pool = res[i].select('td')[14].get_text()
#     print(num, data, red, blue, money, firstnum, firstmoney, secnum, secmoney, pool)
