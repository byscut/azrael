# coding=utf-8
# @Author  : Azrael.Bai
# 题目一
import sys
import json
import copy
import pymongo
import time
import re
import datetime

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from mongo_conf import *
sys.path.append("..")
sys.path.append("../../")

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[ps:%(process)d][line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='clean.log',
                    filemode='w')


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


rdb = get_mongo_client(mongo_app_data_conf)
page_db= get_mongo_client(mongo_page_conf)
wdb = get_mongo_client(mongo_test_data_conf)


class BidExtractor():
    def __init__(self):
        self.zhPattern = re.compile(u'[\u4e00-\u9fa5]+')

        self.plan_aim_pattern = [
            u"一、(.{0,10}?)计划实施目标(.+?)二、",
            u"二、(.{0,10}?)计划实施目标(.+?)三、",
            u"项目简介(.+?)二、",
            u"招标产品简介(.+?)二、",
            u"项目交流说明(.+?)二、",
            u"采购需求(.+?)二、",
            u"本项目目标(.+?)二、",
            u"本项目背景(.+?)二、",
            u"项目概况(.+?)二、",
            u"本项目初步计划实施目标(.+?)二、"
        ]

    def get_planaim_content(self, content):
        for reg in self.plan_aim_pattern:
            seach = re.search(re.compile(reg), content)
            if seach:
                result = seach.group(1)
                return result
            else:
                continue
        return ''

    def get_planaim_content2(self, content):
        for reg in self.plan_aim_pattern:
            result = re.compile(reg).findall(content)
            if result:
                if isinstance(result[0],tuple):
                    return re.sub(u'(（|\().+?(）|\))', u' ', reg)[3:-3] + result[0][1]
                return re.sub(u'(（|\().+?(）|\))', u' ', reg)[:-3] + result[0]
            else:
                continue
        return ''

    def format_extract_data(self, extract_data):
        '''实体解析抽取数据'''
        entity_data = copy.deepcopy(extract_data)


        content = entity_data.get('content','')
        pro_title_reg = u"广东省机电设备(.+?)受广东省信用合作清算中心的委托，就(.+?)发布招标预公告"
        reg = re.compile(pro_title_reg)
        pro_title = ""
        result = reg.findall(content)
        if len(result) > 0:
            pro_title = result[0][1]
            if pro_title.endswith('采购'):
                pro_title = pro_title.replace('采购','')

        if not pro_title:
            title = extract_data.get("title","")
            pro_title = title.split("招标")[0]
            if pro_title == title:
                pro_title = title.split("项目")[0] + "项目"

        plan_and_aim = ""
        # 实施计划和目标
        plan_and_aim = self.get_planaim_content2(content)
        if not plan_and_aim:
            print content

        entity_data['plan_and_aim'] = plan_and_aim
        entity_data['pro_title'] = pro_title


        return entity_data



obj = BidExtractor()


def clean():

    cursor = rdb.get_collection('gdebidding').find({}).batch_size(16)
    extract_data = {}
    count = 0
    a = 0
    b = 0
    for item in cursor:
        try:
            count += 1
            # print count
            extract_data = item

            entity_data = obj.format_extract_data(extract_data)
            entity_data['_utime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # rdb.get_collection("gdebidding").save(entity_data)

            print "case",entity_data.get("pro_title","")


        except Exception,e:
            info = e.message + str(item.get('_id'))
            logging.debug(info)

    print "count",count
    print "a",a
    print "b",b

if __name__ == "__main__":
    '''注意运行时的读写数据库位置'''
    clean()
    '''
    60个有"计划实施目标"
    7个"项目简介"
    1个"招标产品简介"
    1个"项目交流说明"
    1个"采购需求"
    1个"本项目目标"
    1个"本项目背景"
    1个"项目概况"
    '''