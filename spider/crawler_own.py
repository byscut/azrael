#!/usr/bin/Python
# coding=utf-8

import re
import json
import urllib2

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from BeautifulSoup import BeautifulSoup

class GsxxCrawler:
    def __init__(self,id,urls):
        self.id = id
        self.urls = urls
        self.content = {}
        self.parse = {}

    def work(self):
        for url in self.urls:
            self.crawler(url)
            self.parser(url)
        # self.write_json()




    def crawler(self,url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        self.content[url] = response.read()

    def parser(self,url):
        content = json.loads(self.content[url])
        datas = content.get("data",[])
        for data in datas:
            name = data.get("name","")
            table_name = data.get("table_name","")
            print name + "\t" + table_name

    def write_json(self,file =''):
        file = ''
        if not file:
            file = self.id + '.json'

        for key in self.parse.keys():
            print key, self.parse[key]

        with open(file, 'w') as f:
            json.dump(self.parse, f)

if __name__ == '__main__':
    urls = ['http://182.61.37.114:18080/api/topic/entry?name=&pageno=1&table=',
            'http://182.61.37.114:18080/api/topic/entry?name=&pageno=2&table=',
            'http://182.61.37.114:18080/api/topic/entry?name=&pageno=3&table=']
    id = "1"
    obj = GsxxCrawler(id,urls)
    obj.work()
    #obj.parser('http://ah.gsxt.gov.cn/business/JCXX.jspx?id=DC436F2D5F2952118CDEB15D7F0EE103&date=Fri%20Jul%2014%202017%2010:18:08%20GMT+0800%20(CST)')