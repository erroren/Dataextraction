str = """
<bookstore>
    <book>
        <title lang="eng">Harry Potter</title>
        <price>29.99</price>
    </book>
    <book>
        <title lang="eng">Learning XML</title>
        <price>39.95</price>
    </book>
    <coffee id='cof1'>
        <name type="coffee">卡布奇洛</name>
        <price>15</price>
    </coffee>
    <coffee id='cof2'>
        <name type="coffee">拿铁</name>
        <price>25</price>
    </coffee>
</bookstore>
"""

from lxml import etree

# html = etree.HTML(str)
# res = etree.tostring(html).decode()
# print(res)
root = etree.XML(str)
# res = root.xpath('.')
# res = root.xpath('/bookstore/book/price/text()')
res = root.xpath('//book')
# res = root.xpath('//book/..')
res = root.xpath('//book/title/@lang')
# res = root.xpath('//book[1]')
# res = root.xpath('/bookstore/book[last()-1]')
# res = root.xpath('/bookstore/coffee[position()<2]')
# res = root.xpath('/bookstore/book/title[@lang="eng"]')
# res = root.xpath('/bookstore/book[price>30]/title/text()')
# res = root.xpath('//coffee[contains(@id,"1")]')
# for r in res:
#     print(etree.tostring(r))
for r in res:
    print(r)