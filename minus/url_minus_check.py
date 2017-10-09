# coding=utf-8

list1 = []
with open('ex.txt','r') as pre:
    for line in pre:
        line = line.split('url:')[1].split('\tstruct_type')[0]
        list1.append(line)

list2 = []
with open('ex2.txt','r') as latter:
    for line in latter:
        line = line.split('解析成功: ')[1].split(' ')[0]
        list2.append(line)

list3 = [x for x in list1 if x not in list2]

for x in list3:
    print 'url',x

print "length of list1", len(list1)
print "length of list2", len(list2)
print "length of list3", len(list3)
