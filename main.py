#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
from flask import Flask
from flask import render_template
from flask import request
import hashlib

app = Flask(__name__)
dict_set = set()
dict_md5 = {}
dict_md5_rev = {}


@app.route('/')
def search():
    return render_template('search.html')


def response_headers(content):
    resp = response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'    
    return resp 


def read_file(file):
    with open(file, 'r', encoding='utf-8') as fr:
        for line in fr:
            dict_set.add(line.strip())


def md5():
    print('Calculating MD5...')
    print(dict_set.__len__())

    for k in dict_set:
        pwd_md5 = hashlib.md5()
        pwd_md5.update(k.encode('utf-8'))
        v = pwd_md5.hexdigest()
        # dict_md5[k] = v
        # dict_md5[k] = v
        dict_md5_rev[v] = k


#获取登录参数及处理
@app.route('/search')
def search_md5():

    hash = request.args.get('hash')

    try:
        if hash in dict_md5_rev.keys():
            print('find')
            return dict_md5_rev[hash]
        else:
            return 'Not Found'
    except:
        return 'Error'


if __name__ == '__main__':

    # 加载字典文件,生成md5小彩虹表
    read_file('dict/dict.txt')
    read_file('dict/top10W.txt')

    md5()

    app.run(port=5050, debug=True)

