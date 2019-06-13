from urllib import request, parse
if __name__ == '__main__':
    name = input('请输入贴吧名')
    bnum = int(input('起始页码'))
    endnum = int(input('结束页码'))
    for i in range(int(bnum)-1, int(endnum)):
        url = 'http://tieba.baidu.com/f'
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }
        data = {
            'kw': name,
            'ie': 'utf-8',
            'pn': str(i*50),
            'pagelets': 'frs-list/pagelet/thread',
            'pagelets_stamp': '1557747694515'
        }
        data = parse.urlencode(data).encode('utf-8')
        req = request.Request(url, headers=headers)
        response = request.urlopen(req, data=data)
        html = response.read().decode('utf-8')
        with open('./第'+str(i+1)+'页.html', 'w', encoding='utf-8') as file1:
            file1.write(html)