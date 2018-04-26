# -*- coding:utf-8 -*-
from werkzeug.routing import BaseConverter
from flask import Flask,redirect,url_for,render_template,request,json,abort
# 创建应用
app = Flask(__name__, static_folder='static', template_folder='templates')

# 自定义类型转换器
class RegexConverter(BaseConverter):
    regex = '[0-9]{3}'

# 将设置好的转换器导入
app.url_map.converters['re'] = RegexConverter


# 设置DEBUG 导入模式
app.config.from_pyfile('config.conf')


# 设置路由和视图函数
@app.route('/index/<int:order_id>', methods=['GET', 'POST'])
def index(order_id):
    method = request.method
    return 'Hello,Flask%s method is %s'% (order_id,method)

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/')
def index2():
    return redirect(url_for('index',order_id='222'))

# 返回Json数据
@app.route('/set_json')
def json1():
    a = 10/0
    hello = {'name':'zhangsan','age':18 }
    return json.jsonify(hello)

# abort 返回弹出异常
@app.route('/abort')
def abort1():
    abort(505)

# 捕获异常，并返回友好提示
@app.errorhandler(505)
def interal_server_error(e):
    return '服务器搬家了！'

# 自定义装换器 导入装换器包
from werkzeug.routing import BaseConverter


if __name__ == '__main__':
    app.run()



