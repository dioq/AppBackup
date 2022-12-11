#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3
import json


def insert(content):
    conn = sqlite3.connect("../database/my.db")  # 连接数据库
    c = conn.cursor()
    print("数据库打开成功")

    # 将 JSON 对象转换为 Python 字典
    rev_msg = json.loads(content)
    remarks = rev_msg["remarks"]
    data = rev_msg["data"]

    sql_exist = "select count(*) from keychain where remarks = '{remarks}';".format(remarks=remarks)
    cursor = c.execute(sql_exist)
    num = 0
    for row in cursor:
        num = row[0]
    # conn.commit()  # 执行sql语句

    if num == 0: # 插入数据
        print("添加数据")
        sql = "insert into keychain (remarks,data) values('{remarks}','{data}');".format(remarks=remarks,data=data)
        c.execute(sql)
    else: # 更新数据
        print("改变数据")
        sql = "update keychain set data = '{data}' where remarks = '{remarks}';".format(remarks=remarks,data=data)
        c.execute(sql)

    conn.commit()  # 执行sql语句
    conn.close()  # 关闭数据库连接


def query(remarks):
    conn = sqlite3.connect("../database/my.db")  # 连接数据库
    c = conn.cursor()
    print("数据库打开成功")

    sql_exist = "select count(*) from keychain where remarks = '{remarks}';".format(remarks=remarks)
    cursor = c.execute(sql_exist)
    num = 0
    for row in cursor:
        num = row[0]

    if num == 0:
        conn.commit()  # 执行sql语句
        print("查询结束")
        conn.close()  # 关闭数据库连接
        return None

    sql = "select data from keychain where remarks = '{remarks}';".format(remarks=remarks)
    cursor = c.execute(sql)
    data = ""
    for row in cursor:
        data = row[0]
        # print(data)

    conn.commit()  # 执行sql语句
    print("查询结束")
    conn.close()  # 关闭数据库连接
    return data
