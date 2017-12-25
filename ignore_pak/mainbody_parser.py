# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 上午10:45
# @Author  : Azrael.Bai
# @File    : mainbody_parser.py

import re
import pymongo
import time


import sys
reload(sys)
sys.setdefaultencoding("utf-8")


from BeautifulSoup import BeautifulSoup
dict = {u'www.gsei.com.cn': 28171, u'www.lntb.gov.cn': 2, u'www.zbs365.com': 2260, u'www.tjgp.gov.cn': 2,
        u'oss.aliyuncs.com': 837, u'www.ccgp-hunan.gov.cn': 81, u'www.dxggzy.com': 1156, u'www.hljcg.gov.cn': 3,
        u'www.chinabidding.org.cn': 6884, u'www.cnbidding.com': 8876, u'www.lnsggzyjy.cn': 3491, u'www.zyggzy.com': 1,
        u'zb.cbi360.net': 29883, u'www.bidding.hunan.gov.cn': 1, u'www.8yu.cn': 1097, u'www.zgazxxw.com': 40650,
        u'www.plsggzyjy.cn': 7136, u'www.ccgp.gov.cn': 3145, u'www.gszfcg.gansu.gov.cn': 44340,
        u'www.gdzbtb.gov.cn': 14, u'www.gzzbw.cn': 20, u'www.chinabidding.com': 890, u'www.ztb365.cn': 78,
        u'www.lxggzyjy.com': 2544, u'www.wwggzy.com': 8912, u'www.bidcenter.com.cn': 10, u'www.zhaobiao.info': 22531,
        u'www.qianlima.com': 179, u'ztb.hainan.gov.cn': 16, u'www.ccgp-jiangsu.gov.cn': 7, u'www.bygzjy.cn': 424,
        u'www.gzg2b.gov.cn': 2, u'www.gnggzyjy.com': 35, u'www.qyggzyjy.gov.cn': 453}

dict_table = {u'www.gsei.com.cn': 'gsei.com.cn', u'www.lntb.gov.cn': 'lntb.gov.cn', u'www.zbs365.com': 'zbs365.com', u'www.tjgp.gov.cn': 'tjgp.gov.cn',
        u'oss.aliyuncs.com': '无', u'www.ccgp-hunan.gov.cn': 'ccgp-hunan.gov.cn', u'www.dxggzy.com': 'dxggzy.com', u'www.hljcg.gov.cn': 'hljcg.gov.cn',
        u'www.chinabidding.org.cn': 'chinabidding.org.cn', u'www.cnbidding.com': 'cnbidding.com', u'www.lnsggzyjy.cn': '无', u'www.zyggzy.com': '无',
        u'zb.cbi360.net': 'cbi360.net', u'www.bidding.hunan.gov.cn': 'hunan.gov.cn', u'www.8yu.cn': '8yu.cn', u'www.zgazxxw.com': 'zgazxxw.com',
        u'www.plsggzyjy.cn': '无', u'www.ccgp.gov.cn': 'ccgp.gov.cn', u'www.gszfcg.gansu.gov.cn': 'gansu.gov.cn',
        u'www.gdzbtb.gov.cn': 'gdzbtb.gov.cn', u'www.gzzbw.cn': 'gzzbw.cn', u'www.chinabidding.com': 'chinabidding.com', u'www.ztb365.cn': 'ztb365.com',
        u'www.lxggzyjy.com': '无', u'www.wwggzy.com': '无', u'www.bidcenter.com.cn': 'bidcenter.com.cn', u'www.zhaobiao.info': 'zhaobiao.info',
        u'www.qianlima.com': 'qianlima.com', u'ztb.hainan.gov.cn': 'hainan.gov.cn', u'www.ccgp-jiangsu.gov.cn': 'ccgp-jiangsu.gov.cn', u'www.bygzjy.cn': '无',
        u'www.gzg2b.gov.cn': 'gzg2b.gov.cn', u'www.gnggzyjy.com': '无', u'www.qyggzyjy.gov.cn': 'qyggzyjy.gov.cn'}


class AutoParseMainbody:
    def __init__(self):
        pass


    def countchn(self, string):
        pattern = re.compile(u'[\u1100-\uFFFDh]+?')
        result = pattern.findall(string)
        chnnum = len(result)            #list的长度即是中文的字数
        possible = chnnum/len(str(string))         #possible = 中文字数/总字数
        return (chnnum, possible)

    def findtext(self, part):
        length = 50000000
        l = []
        for paragraph in part:
            chnstatus = self.countchn(str(paragraph))
            possible = chnstatus[1]
            if possible > 0.15:
                l.append(paragraph)
        l_t = l[:]
        #这里需要复制一下表，在新表中再次筛选，要不然会出问题，跟Python的内存机制有关
        for elements in l_t:
            chnstatus = self.countchn(str(elements))
            chnnum2 = chnstatus[0]
            if chnnum2 < 300:
            #最终测试结果表明300字是一个比较靠谱的标准，低于300字的正文咱也不想要了对不
                l.remove(elements)
            elif len(str(elements))<length:
                length = len(str(elements))
                paragraph_f = elements
                return paragraph_f

            return None

    def parse_content(self, content = ""):
        soup = BeautifulSoup(content)
        part = soup.select('div')
        mainbody = self.findtext(part)
        if mainbody:
            print mainbody
            return str(mainbody)
        else:
            return ''



def get_mongo_client(target_db):
    try:
        conn = pymongo.MongoClient(host=target_db["host"],
                                   port=target_db["port"],
                                   serverSelectionTimeoutMS=60)
        conn[target_db['vname']].authenticate(target_db['username'], target_db['password'])
        database = conn[target_db['name']]
        return database
    except Exception, mongo_exception:
        print "exception in get_mongo_client:%s" % mongo_exception.message
        # self.wrlog("get_mongo_client fail:%s\n" % (traceback.format_exc()))
        time.sleep(1)


if __name__ == '__main__':
    mongo_page_conf = {
        'host': 'mongo0',
        'port': 40042,
        'vname': 'crawl_merge_webpage',
        'name': 'crawl_merge_webpage',
        'username': 'work',
        'password': 'haizhi',
    }


    apm = AutoParseMainbody()
    content = ''
    apm.parse_content(content)