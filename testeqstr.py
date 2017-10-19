# -*- coding: utf-8 -*-
# @Time    : 2017/10/18 下午5:36
# @Author  : Azrael.Bai
# @File    : testeqstr.py
import Levenshtein

a = u'净资产收益率―加权平均(%)'
b = u'净资产收益率—加权平均(%)'
print a.__len__()
print b.__len__()
for i in range(0, a.__len__()):
    print i,":", Levenshtein.distance(a[i], b[i])
for i in range(0, a.__len__()):
    print ord(a[i]), ord(b[i])