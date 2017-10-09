#!/usr/bin/Python
# coding=utf-8
import time
import pymongo

from mongo_conf import mongo_test_data_conf

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


data = "public_bid_company"
file_app = "/Users/haizhi/Downloads/autotest/total_results/bid_detail/2017-08-23/bid_detail_不匹配_2017-08-23_16-57-25_35646.txt"
file_app2 = "/Users/haizhi/Downloads/autotest/total_results/bid_detail/2017-08-23/bid_detail_缺失_2017-08-23_16-57-25_35646.txt"
file_clean="/Users/haizhi/Downloads/autotest/total_results/bid_detail_clean_20170815/2017-08-23/bid_detail_clean_20170815_不匹配_2017-08-23_16-55-15_71303.txt"
list_app = []
list_app2 = []
list_clean = []

with open(file_app,'r') as fa:
    flag = 0
    for line in fa.readlines():
        if line.__contains__(data):
            flag = 1
        elif flag and line.__contains__('字段'):
            flag = 0
            break
        if flag:
            list_app.append(line.strip())

with open(file_app2,'r') as fa:
    flag = 0
    for line in fa.readlines():
        if line.__contains__(data):
            flag = 1
        elif flag and line.__contains__('字段'):
            flag = 0
            break
        if flag:
            list_app2.append(line.strip())

with open(file_clean,'r') as fa:
    flag = 0
    for line in fa.readlines():
        if line.__contains__(data):
            flag = 1
        elif flag and line.__contains__('字段'):
            flag = 0
            break
        if flag:
            list_clean.append(line.strip())

print 'list_app',len(list_app)
print 'list_app2',len(list_app2)
print 'list_clean',len(list_clean)

new_list = [x.split('\t')[0] for x in list_clean]

for x in new_list:
    print x

testdb = get_mongo_client(mongo_test_data_conf)
cursor = testdb.get_collection('bid_detail_clean_20170815')

for x in new_list:
    item = cursor.find_one({'_record_id':x})
    print x
    if item:
        for x2 in item.get('public_bid_company',['字段缺失']):
            print x2
        print "=========="