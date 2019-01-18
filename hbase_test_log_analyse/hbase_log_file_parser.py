# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 16:47
# @Author  : Azrael.Bai
# @File    : hbase_log_file_parser.py
import os
from logger import AppLogger

def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        yield child

if __name__ == '__main__':
    log = AppLogger('hbase_log.log').get_logger()

    log.info("start analyse ....")
    for file_name in eachFile('../DATAS/hbase_logoutput/'):
        with open(file_name, 'r') as pfile:
            count = 0
            max = 0
            for line in pfile.readlines():
                if line.strip().split('\t').__len__() == 2:
                    sec = line.strip().split('\t')[1]
                    try:
                        if int(sec) > max:
                            max = int(sec)
                        if int(sec) > 100:
                            log.info(line.strip())
                            count += 1
                    except:
                        log.exception('some exception')
            log.info("{} exec long times: {}, max time is :{}".format(file_name, count, max))

    log.info("end analyse ....")