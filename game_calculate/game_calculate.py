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
print i

for a in xrange(0, 31):
    i[0] = a
    print "level0", i[0]
    for b in xrange(0, 31):
        i[1] = b
        print "level1", i[1]
        for c in xrange(0, 31):
            i[2] = c
            print "level2", i[2]
            for d in xrange(0, 31):
                i[3] = d
                print "level3", i[3]
                for e in xrange(0, 31):
                    i[4] = e
                    for f in xrange(0, 31):
                        i[5] = f
                        for g in xrange(0, 31):
                            i[6] = g
                            for h in xrange(0, 31):
                                i[7] = h
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
        fnow = open('out_now_level1'+ str(i[1]) + '.txt', 'w')
        for i in xrange(0, len(max)):
            fnow.write(str(max[i]) + "\t" + ",".join(str(i)) + "\n")
        fnow.close()

print "write..."
f1 = open('out.txt', 'w')
for i in xrange(0, len(max)):
    f1.write(str(max[i]) + "\t" + ",".join(str([i])) + "\n")
f1.close()