# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 上午10:14
# @Author  : Azrael.Bai
# @File    : table_reflect.py


FILE_LIST = [# "ModelDef_GongShang_GSGW.py",
             "ModelDef_GongShang_HZ.py",
             # "ModelDef_GongShang_QCC.py",
             # "ModelDef_GongShang_QXB.py",
             # "ModelDef_SheSu_DFFY.py",
             # "ModelDef_SheSu_HZ.py",
             # "ModelDef_SheSu_QCC.py",
             # "ModelDef_SheSu_QXB.py",
             # "ModelDef_SheSu_ZGFY.py",
             ]
file_write = open("field_with_pojo.txt", 'w')

import re
reg = re.compile("={\'DBColName\'.+?}")

model = ""
if __name__ == '__main__':
    for f in FILE_LIST:
        with open(f, 'r') as filecontent:
            for line in filecontent.readlines():
                if reg.findall(line):
                    str = line.split('=')[1].strip()
                    table_na = re.compile("\'DBColName\':\'(.+?)\'")
                    if table_na.findall(str)[0] == "bold_id":
                        model = line.split('=')[0].strip().replace("_bold_id","")
                    pojo_na = re.compile("\'refPOJOColName\':\'(.+?)\'")
                    pojo_chin = re.compile("\'PGFieldLabel\':\'(.+?)\'")


                    file_write.write(table_na.findall(str)[0]+","+pojo_na.findall(str)[0]+"\n")

file_write.close()
# 排除bold_id，OfCompany，DengJiRen，DengJiShiJian