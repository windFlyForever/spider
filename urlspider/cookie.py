# coding=utf-8
import urllib2
import cookielib

cookieJar = cookielib.CookieJar()

handler = urllib2.HTTPCookieProcessor(cookieJar)

opener = urllib2.build_opener(handler)

req = opener.open('http://www.baidu.com')

cookieStr = ''


for c in cookieJar:
    cookieStr = cookieStr + c.name + '=' + c.value

print cookieStr