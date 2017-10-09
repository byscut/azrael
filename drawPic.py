#!/usr/bin/env python
# coding: utf-8

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 必须配置中文字体，否则会显示成方块
# 注意所有希望图表显示的中文必须为unicode格式
custom_font = mpl.font_manager.FontProperties(size = 6)

font_size = 6 # 字体大小
fig_size = (8, 6) # 图表大小

names = ('2000+app', '10000pages') # 姓名
subjects = ('province', 'judge_content', 'case_cause', 'court', 'case_id', 'doc_content', 'case_type', 'litigants', 'procedure','money_zero','money')
# scores = ((0.7921, 0.9478, 0.8870, 0.9974, 0.9952,
#            1.0, 0.9803, 0.9859, 0.5024, 0.2612, 0.9996),
#           (0.6833, 0.8292, 0.9198, 0.6994, 0.8306,
#            0.9999, 0.8209, 0.8179, 0.6237, 0.4548, 0.9999))
scores = ((0.6833, 0.8292, 0.9198, 0.6994, 0.8306,
           0.9999, 0.8209, 0.8179, 0.6237, 0.4548, 0.9999),
          (0.8299, 0.8293, 0.9214, 0.833, 0.8315,
           0.9477, 0.8218, 0.8185, 0.624, 0.4548, 1.0))
# 更新字体大小
mpl.rcParams['font.size'] = font_size
# 更新图表大小
mpl.rcParams['figure.figsize'] = fig_size
# 设置柱形图宽度
bar_width = 0.35

index = np.arange(len(scores[0]))

rects1 = plt.bar(0.35 + index, scores[0], bar_width, color='#0072BC', label=names[0])

rects2 = plt.bar(0.35 + index + bar_width, scores[1], bar_width, color='#ED1C24', label=names[1])
# X轴标题
plt.xticks(0.35 + index + bar_width, subjects, fontproperties=custom_font)
# Y轴范围
plt.ylim(ymax=1.2, ymin=0)
# 图表标题
plt.title('10000notag', fontproperties=custom_font)
# 图例显示在图表下方
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.03), fancybox=True, ncol=5, prop=custom_font)

# 添加数据标签
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
        # 柱形图边缘用白色填充，纯粹为了美观
        rect.set_edgecolor('white')

add_labels(rects1)
add_labels(rects2)

# 图表输出到本地
plt.savefig('scores_par.png')