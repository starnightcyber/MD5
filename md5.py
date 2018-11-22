#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hashlib
import sqlite3

dict_set = set()
dict_md5 = {}


def read_file(file):
    print('Reading file ...')
    with open(file, 'r', encoding='utf-8') as fr:
        for line in fr:
            dict_set.add(line.strip())
    msg = 'There are {} lines in total...'.format(dict_set.__len__())
    print(msg)


def md5():
    print('Calculating MD5...')
    print(dict_set.__len__())

    for k in dict_set:
        pwd_md5 = hashlib.md5()
        pwd_md5.update(k.encode('utf-8'))
        v = pwd_md5.hexdigest()
        dict_md5[k] = v


def insert2db():
    print('Write to database...')
    conn = sqlite3.connect('md5.db')
    cursor = conn.cursor()
    i = 1

    for k, v in dict_md5.items():
        print(k, '-', v)
        try:
            sql = "INSERT INTO MD5 (ID,PASSWD,PASSWD_MD5)\
                VALUES ('{}', '{}', '{}');".format(i, k, v)
            print(sql)
            cursor.execute(sql)
            i += 1
        except:
            pass

    cursor.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':

    read_file('./dict/dict.txt')
    # read_file('./dict/top10W.txt')

    md5()

    insert2db()
    pass



