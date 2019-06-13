import requests
from lxml import etree


if __name__ == '__main__':
    str1 = int(input("爬取页数:"))

    for i in range(0, str1):
        s = requests.session()
        s.keep_alive = False
        appKey = "UXZrS3IyN1ZyNzhMWjlVSzpidnBMRHJIUkpTUFJpNjJC"
        # 蘑菇隧道代理服务器地址
        ip_port = 'transfer.mogumiao.com:9001'
        url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%89%91%E7%81%B5&fr=search'
        print(url)
        proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
            "Proxy-Authorization": 'Basic ' + appKey
        }
        response = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
        html = response.content.decode()
        root = etree.HTML(html)
        res = root.xpath("//ul[@id='thread_list']/li//a[@class='thumbnail vpic_wrap']/img/@data-original")
        for j in range(len(res)):
            file1 = requests.get(res[j])
            with open('./images/{}.jpg'.format(str(j)), 'wb') as f:
                f.write(file1.content)
                f.flush()
                f.close()
