# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 上午10:01
# @Author  : Azrael.Bai
# @File    : static_province.py


province_dict={}
with open('/Users/haizhi/province.data') as f:
    for line in f.readlines():
        province = line.strip().replace('省','')
        if province_dict.has_key(province):
            province_dict[province] = province_dict[province] + 1
        else:
            province_dict[province] = 1

for key, value in province_dict.items():
    print key, value
