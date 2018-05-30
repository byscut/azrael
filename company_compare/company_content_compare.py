# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 下午6:30
# @Author  : Azrael.Bai
# @File    : company_content_compare.py
import psycopg2
import Levenshtein


class CompanyCompare(object):
    def __init__(self):
        self.conn = psycopg2.connect(database="damp_dev", user="postgres", password="postgres", host="192.168.1.111",
                                     port="5432")

        self.iac_hz_table = [
            'iac_hz_abnormaloperationinfo',
            'iac_hz_baseinfo',
            'iac_hz_branch',
            'iac_hz_changerecordsinfo',
            'iac_hz_changeshareholdinginfo',
            'iac_hz_chattelmortgageinfo',
            'iac_hz_equitypledgedinfo',
            'iac_hz_keyperson',
            'iac_hz_shareholderinfo'
        ]

    def compare(self, company_name):
        # cur = self.conn.cursor()
        # cur.execute("SELECT id, name, address, salary  from COMPANY where company")
        for table in self.iac_hz_table:
            self.compare_list(table, company_name)

    def compare_string(self, company_name, table_name):
        iac_hz_str = "dasagda"
        iac_guanwang_str = "das"

        iac_hz_str = iac_hz_str.replace("\n", "").replace("\r", "")
        iac_guanwang_str = iac_guanwang_str.replace("\n", "").replace("\r", "")

        if not iac_hz_str:
            print "haizhi system lack %s's %s." % (company_name, table_name)
            return 1
        if not iac_guanwang_str:
            print "guanwang lack %s's %s." % (company_name, table_name)
            return 1
        dis = Levenshtein.distance(iac_hz_str, iac_guanwang_str) * 1.0 / max(len(iac_hz_str), len(iac_guanwang_str))
        print "the distence of %s in %s is %f" % (table_name, company_name, dis)
        return dis

    def compare_list(self, company_name, table_name):
        iac_hz_list = [
            [0, 1, 2, 3, 4, 5, 6]
        ]
        iac_guanwang_list = [
            [1, 1, 2, 3, 4, 5, 6]
        ]
        hz_list = [x.replace("\n", "").replace("\r", "") for x in iac_hz_list]
        guanwang_list = [x.replace("\n", "").replace("\r", "") for x in iac_guanwang_list]

        if iac_hz_list is None:
            print "haizhi system lack %s's %s." % (company_name, table_name)
            return
        if iac_guanwang_list is None:
            print "guanwang lack %s's %s." % (company_name, table_name)
            return

        if len(iac_hz_list) == len(iac_guanwang_list):
            print "the length of list %s is same : d%" % (table_name, len(iac_hz_list))
        else:
            print "the length of list %s is different : d%,d%" % (table_name, len(iac_hz_list), len(iac_guanwang_list))

        # 相同的元素数量
        num = 0
        for row in hz_list:
            if row in guanwang_list:
                # guanwang_list.remove(row)
                # hz_list.remove(row)
                num += 1
                continue
            else:
                for row2 in guanwang_list:
                    Levenshtein.distance(row, row2)

if __name__ == '__main__':
    obj = CompanyCompare()
    obj.compare_string("海致星图", '基本信息')