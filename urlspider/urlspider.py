#coding=UTF-8

import urllib2
import random

headers = {
    'host': 'www.taobao.com',
    'connection': 'keep-alive',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': "1",
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-language': 'zh-CN,en-US;q=0.8,en;q=0.6'
}

proxy_list = [
    {"https": "119.101.117.130:9999"},
    {"http": "119.101.112.65:9999"},
    {"https": "119.101.117.223:9999"},
    {"http": "119.101.117.192:9999"},
    {"http": "61.135.217.7:80"}
]

proxy = random.choice(proxy_list)

proxyHander = urllib2.ProxyHandler(proxy)

opener = urllib2.build_opener(proxyHander)

url = 'http://www.taobao.com'
req = urllib2.Request(url, headers=headers)
resp = opener.open(req)
content = resp.read()

print content
print resp.code