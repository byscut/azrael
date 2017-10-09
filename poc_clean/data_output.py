# coding=utf-8
# @Author  : Azrael.Bai
import json
import pymongo
import time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append("..")
sys.path.append("../../")
sys.path.append("../../../")
sys.path.append("../../../../")

from mongo_conf import mongo_app_data_conf
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


def output_gdebidding(database,file_name):

    appdb = get_mongo_client(mongo_app_data_conf)
    cursor = appdb.get_collection(database).find({}).batch_size(16)
    count = 0
    lst = []
    for item in cursor:
        count += 1
        print count
        result = {
            "项目名称":item.get('pro_title',''),
            "计划及实施目标":item.get('plan_and_aim',''),
            "发布时间": item.get('publish_date', '')
        }
        lst.append(result)
    js = {'lst':lst}
    with open(file_name, 'w') as f:
        json.dump(js, f,ensure_ascii=False,indent=4)
        f.write('\n')


def output_chinaland(database,file_name):
    mongo_test_data_conf = {
        'host': '172.16.215.2',
        'port': 40042,
        'vname': 'test',
        'name': 'test',
        'username': 'work',
        'password': 'haizhi',
    }
    testdb = get_mongo_client(mongo_test_data_conf)
    cursor = testdb.get_collection(database).find({}).batch_size(16)
    count = 0
    lst = []
    for item in cursor:
        count += 1
        print count
        for info in item.get('info_list',[]):
            result = {
                "公告标题":item.get('title',''),
                "宗地编号":info.get('land_id',''),
                "宗地总面积":info.get('land_area',''),
                "宗地坐落":info.get('land_location',''),
                "投资强度":info.get('investment',''),
                "起始价":info.get('least','')
            }
            lst.append(result)

    js = {'lst': lst}
    with open(file_name, 'w') as f:
        json.dump(js, f,ensure_ascii=False,indent=4)
        f.write('\n')


def output_chinaland2(database,file_name):
    mongo_test_data_conf = {
        'host': '172.16.215.2',
        'port': 40042,
        'vname': 'test',
        'name': 'test',
        'username': 'work',
        'password': 'haizhi',
    }
    testdb = get_mongo_client(mongo_test_data_conf)
    cursor = testdb.get_collection(database).find({}).batch_size(16)
    count = 0
    lst = []
    for item in cursor:
        count += 1
        print count
        info_list = []

        for info in item.get('info_list',[]):
            info = {
                "宗地编号": info.get('land_id', ''),
                "宗地总面积": info.get('land_area', ''),
                "宗地坐落": info.get('land_location', ''),
                "投资强度": info.get('investment', ''),
                "起始价": info.get('least', '')
            }
            info_list.append(info)

        result = {
            "公告标题": item.get('title', ''),
            "info_list": info_list
        }
        lst.append(result)

    js = {'lst': lst}
    with open(file_name, 'w') as f:
        json.dump(js, f,ensure_ascii=False,indent=4)
        f.write('\n')


if __name__ == '__main__':
    '''注意运行时的读写数据库位置'''
    output_gdebidding('gdebidding','gdebidding.json') # 默认读app_data库
    output_chinaland('land_china_clean0819_3','chinaland.json') # 默认读test库
    output_chinaland2('land_china_clean0819_3','chinaland2.json') # 默认读test库