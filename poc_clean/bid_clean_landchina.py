# coding=utf-8
# @Author  : Azrael.Bai
# 题目二
import json
import copy
import pymongo
import time
import re
import datetime

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append("..")
sys.path.append("../../")

from tools.date_parser import out_date
from mongo_conf import *
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


    def format_extract_data(self, extract_data):
        '''实体解析抽取数据'''
        entity_data = copy.deepcopy(extract_data)
        publish = entity_data.get('publish_date','').strip()
        info_list = entity_data.get('info_list',[])
        content = entity_data.get('content','').strip()
        # source_page = entity_data.get('source','')
        url =  entity_data.get('url','')
        if publish:
            publish = out_date(publish)
            publish = publish.strip()

        new_list = []
        if info_list:
            start_pos = 0
            for info in info_list:
                if not info.get('land_id',''):
                    continue

                # print info['least'],len(info['least'])
                # 如果捕获到其他信息则置空
                if len(str(info.get('least','')))>17 and not info.get('least','').__contains__('起始价'):
                    info['least'] = ""

                # 置空后从正文中提取
                if info['least'] == "":
                    find_ = content.find("起始价")
                    find_least = content.find("起始价",start_pos + 3)
                    if find_least > 0:
                        start_pos = find_least
                        least_content = content[find_least:find_least + 30]
                        info['least'] = least_content.split("加价")[0].strip()
                        info['least'] = info['least'].replace("起始价：","").strip()


                sp = info.get('least','').strip().split('起始价')
                info['least'] = sp[len(sp) - 1].replace("：","").replace(":","").strip()
                # print url
                # print info['least']
                # print "==========="
                info['land_id'] = info.get('land_id', '').strip()
                info['land_area'] = info.get('land_area', '').strip()
                info['land_location'] = info.get('land_location', '').strip()
                info['investment'] = info.get('investment','').strip()
                new_list.append(info)

        if entity_data.has_key('source'):
            del entity_data['source']

        entity_data['content'] = content

        entity_data['publish_date'] = publish
        entity_data['info_list'] = new_list

        return entity_data


def clean():
    obj = BidExtractor()
    cursor = wdb.get_collection('landchina0819').find({}).batch_size(16)
    extract_data = {}
    count = 0

    for item in cursor:
        try:
            count += 1
            print count
            extract_data = item

            entity_data = obj.format_extract_data(extract_data)
            entity_data['_utime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # wdb.get_collection("land_china_clean0819_4").insert(entity_data)
            print  "insert success"
            print "case",entity_data.get("title","")

            # for key, value in entity_data.items():
            #     if isinstance(value, list):
            #         for i in value:
            #             if isinstance(i, dict):
            #                 for key2, value2 in i.items():
            #                     print key2, ":", value2
            #     elif isinstance(value, dict):
            #         for key2, value2 in value.items():
            #             print key2, ":", value2
            #     else:
            #         if key != "source" and key != "content":
            #             print key, ":", value
            # print "======================================"
        except Exception,e:
            info = e.message + str(item.get('_id'))
            logging.debug(info)


if __name__ == "__main__":
    '''注意运行时的读写数据库位置'''
    clean()

