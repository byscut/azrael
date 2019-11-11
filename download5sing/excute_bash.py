# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 09:50
# @Author  : Azrael.Bai
# @File    : excute_bash.py

# coding:utf-8
import subprocess
import sys
import time
import os
import io

def read(filename):
    fh = io.open(filename, 'r', encoding='utf-8')
    lines = fh.readlines()
    fh.close()
    return lines

lines = read('music_save/music_url.sh')

for line in lines:
    cmd = line.replace('\n', '')
    print(cmd)
    f = subprocess.Popen(cmd)
    time.sleep(1)
