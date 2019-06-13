from urllib import request, parse
import json
# url = 'https://movie.douban.com/j/new_search_subjects?'
url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'
# url = 'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action='
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}
data = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
    # 'sort': 'U',
    # 'range': '0,10',
    # 'tags': '',
    # 'start': '0',
    # 'genres': '喜剧'
    # 'type_name': '喜剧',
    # 'type': '24',
    # 'interval_id': '100:90',
    # 'action': ''
}
data = parse.urlencode(data).encode(encoding='UTF8')
req = request.Request(url, data=data, headers=headers)
response = request.urlopen(req)
html = response.read().decode('utf-8')
# print(html)
translate_res = json.loads(html)
# translate_res = translate_res['data']
for i in translate_res:
    print('影名:', i['title'], '评分:', str(i['rating'][0]), '评论数:', i['vote_count'])
    # print(i)