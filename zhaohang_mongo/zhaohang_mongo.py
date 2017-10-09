#!/usr/bin/env python
# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json

import pymongo

from my_setting import TestDataDB

client = pymongo.MongoClient(host=TestDataDB.MONGODB_SERVER, port=TestDataDB.MONGODB_PORT)
db_auth = client.admin
db_auth.authenticate(TestDataDB.MONGO_USER, TestDataDB.MONGO_PSW)
db = client[TestDataDB.MONGODB_DB]
# a= db["bid_detail"].find({"_utime":{"$gte":"2017-09-05","$lte":"2017-09-12"},"_src.0.site":"www.chinabidding.com"}, no_cursor_timeout=True).count()
# cursor = db["bid_detail"].find(
#     {"_src.0.site": "www.chinabidding.com"},
#     no_cursor_timeout=True).sort([("_utime", -1)]).limit(10)
# with open("aaaa.txt", "w") as f:
#     for item in cursor:
#         item["_id"]=str(item["_id"])
#         # print item
#         f.write(json.dumps(item,ensure_ascii=False, indent=4))

b = db["bid_detail"].find({"_src.0.site": "www.guangxibid.com.cn"}, no_cursor_timeout=True).count()
print 'b', b


list_table = ['enterprise_data_gov',
              'baidu_news',
              'bid_detail',
              'land_auction',
              'judgement_wenshu',
              'court_ktgg',
              'judge_process',
              'bulletin',
              'enterprise_owing_tax',
              'shixin_info',
              'zhixing_info',
              'penalty',
              'patent',
              'annual_reports',
              'investment_events',
              'financing_events',
              'acquirer_event',
              'exit_event',
              'tax_payer_level_A',
              'tax_payer_level_A_new']

for table_name in list_table:
    count = 0
    a = db[table_name].find({'_in_time':{'$gte':'2017-09-16 00:00:00'}}, no_cursor_timeout=True).count()
    print table_name, a
