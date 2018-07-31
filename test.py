# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 下午5:29
# @Author  : Azrael.Bai
# @File    : test.py

print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

# from __future__ import print_function
# import random
# while 1:
#     print(random.choice('|| __'), end='')