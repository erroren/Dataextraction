from urllib import request
import chardet

url = 'https://weibo.com/u/6496331216/home'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control':'no-cache, must-revalidate',
    'Connection': 'keep-alive',
    'Cookie': 'Ugrow-G0=56862bac2f6bf97368b95873bc687eef; login_sid_t=ec3dfc5ed627d63722dd9dbfa00f72c0; cross_origin_proto=SSL; YF-V5-G0=d30fd7265234f674761ebc75febc3a9f; wb_view_log=1920*10801; _s_tentry=passport.weibo.com; Apache=7153677989304.339.1557748901764; SINAGLOBAL=7153677989304.339.1557748901764; ULV=1557748901775:1:1:1:7153677989304.339.1557748901764:; WBtopGlobal_register_version=5c10f3128cf400c5; wb_view_log_6496331216=1920*10801; WBStorage=dbba46d4b213c3a3|undefined; SSOLoginState=1557750686; wvr=6; UOR=,,graph.qq.com; webim_unReadCount=%7B%22time%22%3A1557750726518%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A2%2C%22msgbox%22%3A0%7D; crossidccode=CODE-gz-1Hqa9T-2gmSKQ-DFHdPIgk3iScMHSf1afe1; ALF=1589286864; SUB=_2A25x3RQBDeRhGeBK4lQS8y_OyjqIHXVSqwLJrDV8PUNbmtBeLVDAkW9NR3kxgDSzPKSQv8rkxd9hADwVSxX41JK_; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFzMVHjgjWlPlLX8dPw4OgD5JpX5KzhUgL.FoqX1Kq0e02EeKq2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMcSh.ce0epeo2c; SUHB=0nl-37ZexzFg6c; YF-Page-G0=89906ffc3e521323122dac5d52f3e959|1557750888|1557750690',
    'Host': 'weibo.com'

}
req = request.Request(url, headers=headers)
response = request.urlopen(req)
html = response.read().decode()
print(html)
