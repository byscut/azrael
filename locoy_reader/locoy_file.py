# -*- coding: utf-8 -*-
# @Time    : 2017/9/21 上午10:02
# @Author  : Azrael.Bai
# @File    : locoy_file.py
import os


class Locoy(object):
    def __init__(self,out):
        if not os.path.exists(out.replace('/','')):
            os.mkdir(out)
        else:
            if os.path.isfile(out.replace('/','')):
                print out.replace('/',''), '是文件,已经存在'
                quit()
            else:
                print out, '是文件夹,已经存在,将覆盖'
        self.out = out
        self.quantity_check_file = open(out + 'QUANTITY_check_file.txt', 'w')
        self.quality_check_file = open(out + 'QUALITY_check_file.txt', 'w')
        self.error_file = open(out + 'error_file.txt', 'w')
        self.section_statistics_file = open(out + 'statistics_file.txt', 'w')

    def __del__(self):
        self.quality_check_file.close()
        self.quantity_check_file.close()
        self.error_file.close()
        self.section_statistics_file.close()

    def read_locoy_file(self, file_name):
        strall = ''
        with open(file_name, 'r') as pre:
            for str1 in pre.readlines():
                strall = strall + str1
        strsplit = strall.split('====================\n')
        count = 0
        for x in strsplit:
            content = x.strip()
            count += 1
            print str(count) + '. ' + content

    def static_locoy_file(self, file_name):
        strall = ''
        with open(file_name, 'r') as pre:
            for str1 in pre.readlines():
                strall = strall + str1
        strsplit = strall.split('====================\n')
        strsplit = [x.strip() for x in strsplit]
        print len(strsplit)
        if len(strsplit) == 9:
            self.quality_check_file.write('标题:' + strsplit[0] + '\n')
            if len(strsplit[0]) == 0:
                self.error_file.write(file_name + '标题为空,注意检查!!\n')
                self.error_file.flush()
            self.quality_check_file.write('正文长度:' + str(len(strsplit[1])) + '\n')
            if len(strsplit[1]) == 0:
                self.error_file.write(file_name + '正文为空,注意检查!!\n')
                self.error_file.flush()
            # print '站点:' + strsplit[2]
            # print '主题:' + strsplit[3]
            # print '脚本名:' + strsplit[4]
            self.quality_check_file.write('日期:' + strsplit[5] + '\n')
            if len(strsplit[5]) == 0:
                self.error_file.write(file_name + '日期为空,注意检查!!\n')
                self.error_file.flush()
            # print '省份:' + strsplit[6]
            # print '城市:' + strsplit[7]
            self.quality_check_file.write('源代码长度:' + str(len(strsplit[8])) +'\n')
            if len(strsplit[8]) < 300:
                self.error_file.write(file_name + '源代码过短,注意检查!!\n')
                self.error_file.flush()
            self.quality_check_file.write('==========|||==========================|||==========\n')
            # 较为固定字段检查
            return (strsplit[2], strsplit[3], strsplit[4], strsplit[6], strsplit[7])
        return ('', '', '', '', '')

    def static_locoy_file_news(self, file_name):
        strall = ''
        with open(file_name, 'r') as pre:
            for str1 in pre.readlines():
                strall = strall + str1
        strsplit = strall.split('====================\n')
        strsplit = [x.strip() for x in strsplit]
        print len(strsplit)
        if len(strsplit) == 7:
            self.quality_check_file.write('标题:' + strsplit[0] + '\n')
            if len(strsplit[0]) == 0:
                self.error_file.write(file_name + '标题为空,注意检查!!\n')
                self.error_file.flush()
            self.quality_check_file.write('正文长度:' + str(len(strsplit[1])) + '\n')
            if len(strsplit[1]) == 0:
                self.error_file.write(file_name + '正文为空,注意检查!!\n')
                self.error_file.flush()

            self.quality_check_file.write('日期:' + strsplit[5] + '\n')
            if len(strsplit[5]) == 0:
                self.error_file.write(file_name + '日期为空,注意检查!!\n')
                self.error_file.flush()

            self.quality_check_file.write('源代码长度:' + str(len(strsplit[6])) +'\n')
            if len(strsplit[6]) < 300:
                self.error_file.write(file_name + '源代码过短,注意检查!!\n')
                self.error_file.flush()
            self.quality_check_file.write('==========|||==========================|||==========\n')
            # 较为固定字段检查
            return (strsplit[2], strsplit[3], strsplit[4], 'default', 'default')
        return ('', '', '', '', '')

    def find_all_file(self, dir_name):
        for root, dirs, files in os.walk(dir_name):
            if len(os.listdir(root)) == 0:
                self.error_file.write('文件夹 [{}] 是空的,注意检查!!\n'.format(root))
            else:
                self.quantity_check_file.write('文件夹 [{}] 中共有{}个文件,{}个文件夹.\n'.format(root, len(files), len(dirs)))

                dict_f = {}
                flag = True
                for x in files:  # 当前路径下所有非目录子文件
                    file_name = root + '/' + x
                    self.quality_check_file.write(file_name+'\n')
                    print file_name
                    if flag:
                        self.error_file.write("====================================================\n")
                        self.error_file.write("文件夹[{}]中共有[{}]个文件.\n".format(root, len(files)))
                        flag = False
                    tuples = self.static_locoy_file(file_name)
                    for single in tuples:
                        if dict_f.has_key(single):
                            dict_f[single] += 1
                        else :
                            dict_f[single] = 1
                if len(files) > 0:
                    self.section_statistics_file.write('====================================================\n')
                    self.section_statistics_file.write(self.out + root.replace('/', '_') + '\n')
                    for key in dict_f.keys():
                        self.section_statistics_file.write(key + '\t' + str(dict_f[key]) + '\n')
                    self.section_statistics_file.flush()

def run_0920():
    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/zhanghang/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/0930/张航/0920张航/')
    # obj.read_locoy_file('datas/source_file/芙蓉区政府采购网.txt')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/wangqing/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/0930/王青/0920王青/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/fangyang/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/0930/方洋/0920样本/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/xiaoshaoxuan/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/0930/肖少旋/火车头本地保存/')

def run_0929():
    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/zhanghang/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/1009/张航/张航0929/')
    # obj.read_locoy_file('datas/source_file/芙蓉区政府采购网.txt')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/wangqing/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/1009/王青/今日采集任务1009/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/fangyang/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/1009/方洋/09.29/')

def run_1114():
    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/1114/chenying/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/1114/陈迎/采集/')

def run_1118():
    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/1118临时/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/1114/方洋临时/1118/1118/')



if __name__ == '__main__':
    run_1118()