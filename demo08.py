from bs4 import BeautifulSoup

html = """ 
<html>
    <head><title>The Dormouse's story</title></head>
    <body> 
        <p class="title" name="dromouse"><b>The Dormouse's story</b></p> 
        <p class="story">Once upon a time there were three little sisters; and their names were 
        <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --><!-- Elsie --></a>, 
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; 
        and they lived at the bottom of a well.</p> <p class="story">...</p> 
"""
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.head)
# print(type(soup.head))
# print(soup.head.title.name)
# print(soup.p.attrs)
# print(soup.p['name'])
# soup.p['class']='tttile'
# del soup.p['class']
# print(soup.p)
# print(soup.p.string)
# s = soup.a.contents
# s = soup.p.children
# s = soup.descendants
# for i in s:
#     print(i)
# print(soup.select('a')[2])
# print(soup.select('body .title'))
print(soup.select('a')[1].get_text())