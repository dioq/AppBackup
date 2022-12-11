#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, request
import json
import dbutil

app = Flask(__name__)


def test1():
    data = {
        'remarks': 'wx5',
        'data': 't2.jobs8.cn'
    }
    json_str = json.dumps(data)
    dbutil.insert(json_str)


@app.route('/backup', methods=['POST'])
def backupAppData():
    body = request.get_json()
    print(body)
    json_str = json.dumps(body)
    dbutil.insert(json_str)

    ret_content = {'code': 200, 'msg': "数据保存成功!"}
    return ret_content, 200


@app.route('/recovery', methods=['GET'])
def recoveryAppData():
    remarks = request.args.get('remarks')  # 获取姓名文本框的输入值
    result = dbutil.query(remarks)
    if result is None:
        msg = "数据库没有这条数据"
        ret_content = {'code': 201, 'msg': msg}
        return ret_content, 201
    else:
        ret_content = {'code': 200, 'msg': "数据获取成功!","content": result}
        return ret_content, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)
