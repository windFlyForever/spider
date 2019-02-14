# coding=utf-8
import requests

#1.创建session对象，可以保存Cookie值
ssion = requests.session()

#2.处理headers
headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}

#3.需要登陆的用户名和密码
data={"email":"mr_mao_hacker@163.com", "passwd":"alarmchime"}

#4.发送附带用户名和密码的请求，并获取登陆后的Cookie的值，保存在session里
ssion.post("http://www.renren.com/PLogin.do", data=data,headers=headers)

#5.ssion包含用户登陆后的cookie值，可以直接访问那些登陆后的页面
response = ssion.get("http://www.renren.com/410043129/profile")

#6.打印响应内容
print(response.text)
