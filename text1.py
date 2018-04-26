# -*- coding:utf-8 -*-

from flask import Flask, redirect, url_for, request
from werkzeug.routing import BaseConverter
# 创建应用
app = Flask(__name__)

# 自定义匹配规则
class NewConverter(BaseConverter):
    regex = '[0-9]{3}'
    # 重写to_python的方法
    def to_python(self, order_id):
        order_id = int(order_id)
        return order_id

app.url_map.converters['re'] = NewConverter
# 设置DEBUG 导入模式
app.config.from_pyfile('config.conf')

# 请求钩子
# 每一次请求前调用
@app.before_first_request
def no1():
    print '---1---'
# 每一次执行前
@app.before_request
def no2():
    print '---2---'
# 视图函数执行后调用
@app.after_request
def no3(response):
    print '---3---'
    return response
# 错误信息调用的
# @app.teardown_request
# def no4(e):
#     print '---4---',e
# 设置路由和视图函数
@app.route('/index')
def index():
    return 'hello world'

# 设置带参数
@app.route('/order/<re:order_id>')
def order(order_id):
    return 'hello world %s'% order_id

# 设置路由重定向和反向解析
@app.route('/demo')
def demo():
    print request.url, request.method
    name = request.args.get('name')
    age = request.args.get('age')
    print 'name=%s,age=%s' % (name,age)
    return redirect(url_for('order',order_id=222))

if __name__ == '__main__':
    app.run()