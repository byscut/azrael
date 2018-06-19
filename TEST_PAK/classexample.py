# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 下午6:52
# @Author  : Azrael.Bai
# @File    : classexample.py

# 万物皆可类
# 这里是类声明
class 人:
    def __init__(self):
        # 拥有这个类的变量都会有这些属性
        self.id = "00000000000"
        self.身高 = 0
        self.体重 = 0
        self.位置 = (0, 0)
        self.学校 = None

    def 成长(self):
        self.id = "1231313511313"
        self.身高 = 150
        self.体重 = 40

    def 继续长大(self):
        self.身高 += 1
        self.体重 += 1

    def 行走(self):
        self.位置 = (1, 0)

    def 学习(self,学校名称):
        self.学校 = 学校名称

# 这里是类调用,声明一个人类型的变量
马思远 = 人()
# 马思远成长了 ,给了一个id,身高体重变化了
马思远.成长()
# 马思远又成大了
马思远.继续长大()
# 马思远会走路了,位置发生了变化
马思远.行走()
# 马思远上学了,要给一个学校名称记录在类的学校字段里
马思远.学习("xxx学校")


