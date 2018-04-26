# -*- coding:utf-8 -*-

from flask import Flask,make_response,request
# 创建应用
app = Flask(__name__)
# 设置DEBUG 导入模式
app.config.from_pyfile('config.conf')
# 设置路由和视图函数
@app.route('/set_cookie')
def index():
    response = make_response('设置成功！')
    response.set_cookie('name','zhuolin',max_age = 3600)
    response.set_cookie('age','18',)
    name = request.cookies.get('name')
    print name
    return response

# 获取cookie
@app.route('/get_cookie')
def demo():
    name = request.cookies.get('name')
    return name

# 删除cookie
@app.route('/del_cookie')
def delect1():
    response = make_response('删除cookie成功！')
    response.delete_cookie('name')
    return response
if __name__ == '__main__':
    app.run()