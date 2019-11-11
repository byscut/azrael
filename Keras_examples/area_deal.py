# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 18:16
# @Author  : Azrael.Bai
# @File    : area_deal.py
# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding("utf8")

from area_dict import *


def get_pcd_from_address(address, province=u"", city=u"", district=u""):
    if not address:
        return province, city, district
    province_set = set(province_list)
    address = address.replace(u"（", u"").replace(u"）", u"")
    if address.startswith(u"中国"):
        address = address[2:]

    if not province:
        province = address[:2]
        if province not in province_set:
            province = u""
        if province in municipality_list:
            city = u"市辖区"

    if province == u"内蒙":
        province = u"内蒙古"
    if province == u"黑龙":
        province = u"黑龙江"

    if address.startswith(province[:2]):
        address = address.strip(province)

    try:
        if address[0] in [u"街", u"路"] or address[1] in [u"街", u"路"]:
            province = u""
    except IndexError:
        pass

    if address.startswith(u"省") or address.startswith(u"市"):
        address = address[1:]
    if address.startswith(u"自治区"):
        address = address[3:]
    if not city:
        if address[:2] == u"张家":
            city = city_head.get(address[:3], u"")
        else:
            city = city_head.get(address[:2], u"")

    # 标记存储
    address_with_city = address
    if address.startswith(city[:2]):
        address = address.strip(city)

    try:
        if address[0] in [u"街", u"路"] or address[1] in [u"街", u"路"]:
            city = u""
    except IndexError:
        pass

    if address.startswith(u"区") or address.startswith(u"县"):
        # 当把区当成市时 重置地址为移除city前
        address = address_with_city

    if not district:
        # 五字区
        if address[:3] in five_district_head:
            district = district_head.get(address[:5], u"")
        # 三字区
        elif address[:2] in three_district_head:
            district = district_head.get(address[:3], u"")
        # 普通区
        else:
            district = district_head.get(address[:2], u"")

    if district not in address:
        district = u""

    if district and not city:
        tmp_city = district_dict.get(district)
        if isinstance(tmp_city, dict):
            if len(tmp_city.keys()) == 1:
                city = list(tmp_city.keys())[0]
                if not province:
                    province = tmp_city[city]
            else:
                if province:
                    for k in tmp_city.keys():
                        if tmp_city[k] == province:
                            city = k

    if city and not province:
        tmp_province = city_dict.get(city, None)
        if tmp_province is not None:
            province = tmp_province
    return province, city, district


def get_pcd_from_code(code):
    try:
        if len(code) < 6:
            return u"", u"", u""
    except:
        return u"", u"", u""
    # 91 92开头要去掉头部两位
    if code.startswith(u"9"):
        code = code[2:8]
    province_code = code[:2]
    city_code = code[:4]
    district_code = code[:6]
    province_data = code_area_dict.get(province_code, {})
    province = province_data.get(u"name", u"")
    city_data = province_data.get(u"city", {}).get(city_code, {})
    city = city_data.get(u"name", u"")
    district = city_data.get(u"district", {}).get(district_code, u"")

    return province, city, district


def get_pcd(company, unified_social_credit_code, address, registered_address):
    # todo: 执行逻辑是补漏 所以把可靠的放在前面
    code_province, code_city, code_district = get_pcd_from_code(unified_social_credit_code)

    # todo: address
    province, city, district = get_pcd_from_address(address, code_province, code_city, code_district)
    # todo: registered_address
    province, city, district = get_pcd_from_address(registered_address, province, city, district)

    # todo: company
    province, city, district = get_pcd_from_address(company, province, city, district)

    if province == u"内蒙":
        province = u"内蒙古"
    if province == u"黑龙":
        province = u"黑龙江"
        # todo:归属关系判断

    if city not in district_dict.get(district, {}).keys():
        district = code_district


    tmp_ = city_dict.get(city)
    if tmp_ == u"内蒙":
        tmp_ = u"内蒙古"
    if tmp_ == u"黑龙":
        tmp_ = u"黑龙江"

    if isinstance(tmp_, list):
        if province not in tmp_:
            city = code_city
            province = code_province
    else:
        if province != tmp_:
            city = code_city
            province = code_province

    if province in municipality_list:
        province_city = province
    else:
        province_city = u"{0}{1}".format(province, city)

    if province_city.endswith(u"市"):
        province_city = province_city[:-1]

    if not city:
        province_city = u""

    if province == u"内蒙":
        province = u"内蒙古"
    if province == u"黑龙":
        province = u"黑龙江"

    return province, province_city, district


def main_run():
    for line in sys.stdin:
        # company,province,city,district,unified_social_credit_code,address,registered_address
        try:
            line = line.strip()
            company = line.split('\t')[0]
            old_province = line.split('\t')[1]
            old_city = line.split('\t')[2]
            old_district = line.split('\t')[3]
            unified_social_credit_code = line.split('\t')[4]
            address = line.split('\t')[5]
            registered_address = line.split('\t')[6]

            province, city, district = get_pcd(company, unified_social_credit_code, address, registered_address)

            print "\t".join(
                [company, old_province, old_city, old_district, province, city, district, unified_social_credit_code,
                 address, registered_address])
        except:
            continue


def test():
    # 乌兰浩特市人民政府, 张家港保税区好客纺织有限公司, 北京市人民政府(直辖市问题),宁乡市食品药品工商质量监督管理局
    test_dict = {
        u'乌兰浩特市人民政府': (u'内蒙古', u'内蒙古兴安盟', u''),
        u'张家港保税区好客纺织有限公司': (u'江苏', u'江苏苏州', u'张家港市'),
        u'北京市人民政府': (u'北京', u'北京', u''),
        u'宁乡市食品药品工商质量监督管理局': (u'湖南', u'湖南长沙', u'宁乡市'),

    }
    company = u"张家港市凤凰镇韩国工业园嘉泰路"
    province, city, district = get_pcd_from_address(company)
    print "company = ", company
    print "province = ", province, "city = ", city, "district = ", district

if __name__ == '__main__':
    test()
