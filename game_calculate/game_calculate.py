# -*- coding: utf-8 -*-
# @Time    : 2018/2/12 下午7:17
# @Author  : Azrael.Bai
# @File    : game_calculate.py
import copy
money = [100,   78,   50,   12,   30,   10,   6,   5]
value = [10800, 8250, 5250, 1250, 3090, 1020, 600, 500]
counts = [0, 0, 0, 0, 0, 0, 0, 0]

# for i in xrange(0,len(money)):
#     print money[i], str(value[i] / money[i])


def plus(value, counts):
    sum = 0
    for i in xrange(0, len(counts)):
        sum = sum + (value[i] * counts[i])
    return sum


def add(lst):
    sum = 0
    for i in xrange(0, len(lst)):
        sum += lst[i]
    return sum

# 每天充值金额≥30，连续充值7天，320≥充值总额≥300
max = []
clist = []

i = [0, 0, 0, 0, 0, 0, 0, 0]
print "calculate..."

for i[0] in xrange(0,31):
    print "level0", i[0]
    for i[1] in xrange(0, 31):
        print "level1", i[1]
        for i[2] in xrange(0, 31):
            print "level2", i[2]
            for i[3] in xrange(0, 31):
                print "level3", i[3]
                for i[4] in xrange(0, 31):
                    for i[5] in xrange(0, 31):
                        for i[6] in xrange(0, 31):
                            for i[7] in xrange(0, 31):
                                if plus(money, i) > 320 or plus(money, i) < 300:
                                    continue
                                elif add(i) < 7:
                                    continue
                                else:
                                    results = plus(value, i) / plus(money, i)
                                    if len(max) < 1000:
                                        max.append(results)
                                        clist.append(copy.deepcopy(i))
                                    else:
                                        min_in_max = min(max)
                                        if results > min_in_max:
                                            mincount = min_in_max
                                            locate = max.index(mincount)
                                            max[locate] = results
                                            clist[locate] = copy.deepcopy(i)
                                        else:
                                            pass
print "write..."
f = open('out.txt', 'w')
for i in xrange(0, len(max)):
    f.write(str(max[i]) + "\t" + ",".join(str([i])) + "\n")
f.close()