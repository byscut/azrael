# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 11:37
# @Author  : Azrael.Bai
# @File    : flask_hello.py
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>hello world</h1>'

if __name__ == '__main__':
    app.run()
