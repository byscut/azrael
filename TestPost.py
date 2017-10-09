#!/usr/bin/Python
# coding=utf-8

import urllib2
import urllib

import sys
reload(sys)
sys.setdefaultencoding('utf8')


url = 'http://www.lz.gansu.gov.cn/module/web/jpage/dataproxy.jsp?startrecord=46&endrecord=90&perpage=15'

head = {
    'Accept': 'application/xml, text/xml, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '146',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'Hm_lvt_86f43783acc56b0c8abb5bb039edc763=1500007944,1500287075; Hm_lpvt_86f43783acc56b0c8abb5bb039edc763=1500348098',
    'Host': 'www.lz.gansu.gov.cn',
    'Origin': 'http://www.lz.gansu.gov.cn',
    'Referer': 'http://www.lz.gansu.gov.cn/col/col122/index.html?uid=4702&pageNum=3',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
param = {
    'col': '1',
    'appid': '1',
    'webid': '1',
    'path': '/',
    'columnid': '122',
    'sourceContentType': '1',
    'unitid': '4702',
    'webname': '兰州市政府',
    'permissiontype': '0',
}
param_code = urllib.urlencode(param)
request = urllib2.Request(url,data=param_code,headers=head)
response = urllib2.urlopen(request)
print response.read().decode('utf8')
