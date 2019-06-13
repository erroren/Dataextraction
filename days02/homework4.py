import requests
from lxml import etree
import time
for i in range(0, 141, 20):
    time.sleep(1)
    s = requests.session()
    s.keep_alive = False
    appKey = "UXZrS3IyN1ZyNzhMWjlVSzpidnBMRHJIUkpTUFJpNjJC"
    # 蘑菇隧道代理服务器地址
    ip_port = 'transfer.mogumiao.com:9001'
    url = 'https://gaokao.chsi.com.cn/sch/search.do?searchType=1&ssdm=41&start='+str(i)
    print(url)
    proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        "Proxy-Authorization": 'Basic ' + appKey
    }
    response = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    html = response.content.decode()
    print(html, type(html))
    # root = etree.HTML(html)
    # res = root.xpath("//table[@class='ch-table']//td[@class='js-yxk-yxmc']/a/@href")
    # sname = root.xpath("//table[@class='ch-table']//td[@class='js-yxk-yxmc']/a/text()")
    # for i in range(len(sname)):
    #     print(sname[i].strip())
    # print(sname)
    # for j in res:
    #     # s1 = requests.session()
    #     # s1.keep_alive = False
    #     # appKey1 = "UXZrS3IyN1ZyNzhMWjlVSzpidnBMRHJIUkpTUFJpNjJC"
    #     # 蘑菇隧道代理服务器地址
    #     # ip_port1 = 'transfer.mogumiao.com:9001'
    #     url1 = "https://gaokao.chsi.com.cn"+j
    #     # proxy1 = {"http": "http://" + ip_port, "https": "https://" + ip_port}
    #     # headers1 = {
    #     #     'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);',
    #     #     "Proxy-Authorization": 'Basic ' + appKey1
    #     # }
    #     # response1 = requests.get(url1, headers=headers1, proxies=proxy1, verify=False, allow_redirects=False)
    #     response1 = requests.get(url1)
    #     html1 = response1.content.decode()
    #     # time.sleep(1)
    #     root1 = etree.HTML(html1)
    #     res1 = root1.xpath("//div[@class='nav-container clearfix']/a[4]/@href")[0]
    #     url2 = 'https://gaokao.chsi.com.cn'+res1
    #     response2 = requests.get(url2)
    #     html2 = response2.content.decode()
    #     root2 = etree.HTML(html2)
    #     res2 = root2.xpath("//div[@class='container']/div[2]/div[@class='ch-tab clearfix']//a/text()")
    #     for res22 in range(len(res2)):
    #         res3 = root2.xpath("//div[@class='container']/div[2]/div[@class='tab-content']/div[{}]//a/text()".format(str(res22+1)))
    #         list1 = []
    #         for i1 in res3:
    #             list1.append(i1)
    #         print(res2[res22],list1)
    #     print("________________")