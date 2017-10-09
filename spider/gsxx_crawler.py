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
        self.write_json()




    def crawler(self,url):
        request = urllib2.Request(url)
        print url
        response = urllib2.urlopen(request)
        self.content[url] = response.read()

    def parser(self,url):
        if url.__contains__('basic.jspx'):
            soup = BeautifulSoup(self.content[url])
            #print soup.prettify()
            find = soup.find(id = 'basic_center')
            if not self.parse.has_key('name') or not self.parse.get('name',''):
                if find.find(id = 'entName'):
                    self.parse['name'] = find.find(id = 'entName').string.strip()
            if not self.parse.has_key('status') or not self.parse.get('status',''):
                if find.find(id = 'zhangtai'):
                    self.parse['status'] = find.find(id = 'zhangtai').string.strip()

            rex_string = '\<p\>\s*\<span class=\"basic-info\"\>((\s|.)+?)\</span\>\s*\<span class=\"label\"\>((\s|.)+?)\</span\>\s*\</p\>'

            #rex_string = ur'<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)'
            regex =re.compile(rex_string)
            regex_get = regex.findall(str(find))
            for reg in regex_get:
                count = 0
                result = []
                for find_str in reg:
                    if count % 2 == 0:
                        result.append(find_str.strip())
                    count += 1
                if len(result) == 2:
                    self.parse[result[0]] = result[1]


        elif url.__contains__('JCXX.jspx'):
            soup = BeautifulSoup(self.content[url])
            # soup = BeautifulSoup(open('JCXX'))
            #print soup.prettify()
            #提取主信息列表
            xinxi_table = soup.find('div',id = 'zhizhao')
            if xinxi_table:
                tds = xinxi_table.findAll('td')
                for td in tds:
                    if td.contents[0] == u'\n':
                        regex = re.compile("\<div class=\"jingyingfanwei\">(.+?)\<span\>(.*?)\</span\>\</div\>")
                        find_tuple = regex.findall(str(td))[0]
                        if len(find_tuple) == 2:
                            self.parse[find_tuple[0].replace(u'&nbsp;',u'').replace(u'·',u'').replace(u'：',u'').strip()] = find_tuple[1].strip()
                    if td.contents[0] and td.span.string:
                        self.parse[td.contents[0].replace(u'&nbsp;',u'').replace(u'·',u'').replace(u'：',u'').strip()] = td.span.string.strip()

            #提取出资人列表
            # chuzi_xinxi = soup.find('div', id = 'paging')#<div id="paging">
            # if chuzi_xinxi:
            #     #print chuzi_xinxi
            #     chuzi_table_head = chuzi_xinxi.find('table',{'class':'detailsList'})
            #     chuzi_table_content = chuzi_xinxi.find('table',{'class':'detailsListGDCZ'})
            #     if chuzi_table_head and chuzi_table_content:
            #         print chuzi_table_head
            #         print '=================='
            #         print chuzi_table_content
            #         print '=================='

            #提取主要人员信息
            zhuyaorenyuan = soup.find('div',style = 'padding-bottom:8px;')#<div class="baseinfo" style="padding-bottom:8px;">
            if zhuyaorenyuan:
                reper = re.compile('<span style=\"color:#333333;\"\>(.+?)\<\/span\>')
                persons = reper.findall(str(zhuyaorenyuan))
                self.parse['persons'] = persons
            #变更信息
            change = soup.find('div',id = 'bgxx').find('table',id = 'alterInfo')#<div class="baseinfo" id="bgxx">
            print change
            print 'r================================='
            if change:
                trs = change.findAll('tr')
                changeInfo = []
                for tr in trs:
                    changeUnit = {}
                    tds = tr.findAll('td')
                    if len(tds) == 5:
                        changeUnit['changeInfo'] = tds[1].string
                        changeUnit['before'] = tds[2].string
                        changeUnit['after'] = tds[3].string
                        changeUnit['date'] = tds[4].string
                    if changeUnit:
                        changeInfo.append(changeUnit)
                self.parse['change'] = changeInfo
            #以上4个够用了
        else:
            print "The url has some problem..."

        # print self.content[url].strip()
        print "================================"



        if not self.parse.get('url'):
            self.parse['url'] = [url]
        else:
            self.parse['url'].append(url)



    def write_json(self,file =''):
        file = ''
        if not file:
            file = self.id + '.json'

        for key in self.parse.keys():
            print key, self.parse[key]

        with open(file, 'w') as f:
            json.dump(self.parse, f)

if __name__ == '__main__':
    urls = ['http://ah.gsxt.gov.cn/company/basic.jspx?id=DC436F2D5F2952118CDEB15D7F0EE103',
            'http://ah.gsxt.gov.cn/business/JCXX.jspx?id=DC436F2D5F2952118CDEB15D7F0EE103&date=Mon%20Jul%2017%202017%2010:20:02%20GMT+0800%20(CST)']
    urls = ['http://ah.gsxt.gov.cn/business/JCXX.jspx?id=DC436F2D5F2952118CDEB15D7F0EE103&date=Mon%20Jul%2017%202017%2010:20:02%20GMT+0800%20(CST)']
    id = "2134545654356"
    obj = GsxxCrawler(id,urls)
    obj.work()
    #obj.parser('http://ah.gsxt.gov.cn/business/JCXX.jspx?id=DC436F2D5F2952118CDEB15D7F0EE103&date=Fri%20Jul%2014%202017%2010:18:08%20GMT+0800%20(CST)')