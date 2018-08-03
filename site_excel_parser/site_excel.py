# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 下午4:30
# @Author  : Azrael.Bai
# @File    : site_excel.py
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     work
   Description :
   Author :       tangxin
   date：          2018/7/27
-------------------------------------------------
   Change Activity:
                   2018/7/27:
-------------------------------------------------
"""
import os

import xlrd


def read_sites():
    dir_path = u'/Users/haizhi/azrael/DATAS/20180803湖南涉诉类站点.xlsx'

    source = xlrd.open_workbook(dir_path)
    source_table = source.sheet_by_index(0)
    source_rows = source_table.nrows
    dict_sites = {}
    for i in xrange(1, source_rows):
        row_data = source_table.row_values(i)

        site = row_data[7].replace('http://', '').replace('https://', '').split('/')[0]
        if site not in dict_sites:
            dict_sites[site] = (row_data[5].split('-')[0],row_data[10])
    statics = read_statistics()
    for key, value in dict_sites.items():
        if key in statics.keys():
            print key + "\t" + value[0] + "\t" + value[1] + "\t" + str(int(statics[key][0])) + "\t" + str(
                int(statics[key][1])) + "\t" + str(int(statics[key][2])) + "\t" + str(int(statics[key][3]))
        else:
            print key + "\t" + value[0] + "\t" + value[1] + "\t0\t0\t0\t0"

def read_statistics():
    dir_path = u'/Users/haizhi/azrael/DATAS/increment-2018-07-31_00_10_07-sites.xls'
    statics = {}
    source = xlrd.open_workbook(dir_path)
    source_table = source.sheet_by_index(0)
    source_rows = source_table.nrows
    dict_sites = {}
    for i in xrange(1, source_rows):
        row_data = source_table.row_values(i)

        site = row_data[1]
        statics[site] = (row_data[4], row_data[5], row_data[6], row_data[7])

    return statics



if __name__ == '__main__':
    read_sites()
