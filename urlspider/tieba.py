#coding=utf-8

import urllib2
import urllib

#https://tieba.baidu.com/f?kw=data2&ie=utf-8&pn=50

headers = {
    'connection': 'keep-alive',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': "1",
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-language': 'zh-CN,en-US;q=0.8,en;q=0.6'
}

kw = raw_input("请输入要爬的贴吧：")
startpage = int(raw_input("输入起始页："))
endpage = int(raw_input("输入结束页："))

url = 'https://tieba.baidu.com/f?'
url = url+urllib.urlencode({'kw': kw})

for page in range(startpage, endpage+1):

    pn = (page-1)*50

    filename = "第"+str(page)+"页.html"

    url = url + "&pn="+str(pn)

    req = urllib2.Request(url, headers=headers)

    resp = urllib2.urlopen(req)

    html = resp.read()

    print '正在下载：'+filename

    fo = open('tieba/%s' % (filename), 'wb+')

    fo.write(html)

    fo.close()
