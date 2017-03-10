# -*- coding: utf-8 -*-
import urllib2
import urllib
#脚本应用于get请求单框注入情况下
#定义一个url
#脚本作用为遍历过滤关键字扫描生成结果中的所有关键字，并确认其属于本人已掌握的sqlinjectionkeyword关键字，然后筛选出第二层结果
url='http://ctf5.shiyanbar.com/423/web/?id=';
#定义关键字测试使用的载荷库
j=0
f = file("test_result_final.txt", "w+")
keyword=[]
for i in open("dict/sqlinjectionkeyword.txt"):
    keyword.append(i.replace("\n",""))
for line in open("test_result.txt"):
    # print get_md5(line.strip()) + ':' + line
    line=line.replace("\n","")
    for k in keyword:
        #print k+'  vs   '+line.lower()
        if(line.lower()==k):
            print line + "\n"
            f.writelines(line + "\n")
f.close()
