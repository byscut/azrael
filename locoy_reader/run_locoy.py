# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 上午10:15
# @Author  : Azrael.Bai
# @File    : run_locoy.py
from locoy_file import Locoy

def run_1127():
    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/1127/张航/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/1121gdnews/张航/1121/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/1127/方洋/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/1121gdnews/方洋/1121/1121/')


def run_1219():
    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/1219/方洋/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/shuju/1121FY/1121/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/1219/张航/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/shuju/1121ZH/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/1219/肖少旋/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/shuju/1121XSX/1108火车头发布/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/12192/方洋/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/shuju/1129FY/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/12192/张航/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/shuju/1129ZH/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/12192/肖少旋/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/shuju/1129XSX/1129紧急新闻/')


def run_1220():
    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/12202/方洋/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/1211bid（紧急）/方洋/1211FY/1211/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/12202/张航/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/1211bid（紧急）/张航/1211/新疆/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/12202/肖少旋/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/1211bid（紧急）/肖少旋/1211招中标任务/新疆/')


    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/12202/陈迎/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/1211bid（紧急）/陈迎/1211招中标任务/1211招中标任务/1211-陈迎-采集/')

def run_201801():
    # # 参数为输出文件夹,注意要带斜杠
    # obj = Locoy('datas/201801/方洋/')
    # # 参数为输入待检查文件夹,注意要带斜杠
    # obj.find_all_file('/Users/haizhi/huochesite_checking/1222xbbid/方洋/1222/1222/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/201801/张航/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/1222xbbid/张航/1222/')

    # # 参数为输出文件夹,注意要带斜杠
    # obj = Locoy('datas/201801/肖少旋/')
    # # 参数为输入待检查文件夹,注意要带斜杠
    # obj.find_all_file('/Users/haizhi/huochesite_checking/1222xbbid/肖少旋/1222招中标火车任务/')


def run_20180102():
    # # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/20180102/方洋/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/20180102bid/方洋/0108以及1222改/0108/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/20180102/张航/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/20180102bid/张航/0108/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/20180102/肖少旋/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/20180102bid/肖少旋/0108招中标任务/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/20180102/陈迎/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/20180102bid/陈迎/0109招中标/采集/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/201801/黄厚华/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/20180102bid/黄厚华/火车采集2/')


def run_20180312():
    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/20180312/陈迎/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/0129/陈迎/陈迎-0129-采集/采集/')

    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/20180312/黄厚华/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/0129/黄厚华/0129hhh/')

if __name__ == '__main__':
    # 参数为输出文件夹,注意要带斜杠
    obj = Locoy('datas/20180312/肖少璇/')
    # 参数为输入待检查文件夹,注意要带斜杠
    obj.find_all_file('/Users/haizhi/huochesite_checking/0129/肖少旋/0129火车配置/')