# -*- coding:utf-8 -*-

from flask import Flask,render_template,g,flash
# 创建应用
app = Flask(__name__)
# 设置DEBUG 导入模式
app.config.from_pyfile('config.conf')
# 设置路由和视图函数
app.config['SECRET_KEY'] = 'jvmw0c-_977ik9obgz1(r$t@q_vi0yk4-$y8rv$mf9dm2la=b3'
# 自定义过滤器
@app.template_filter('listReverse')
def do_listreverse(list):
    list.reverse()
    return list

@app.route('/')
def index():
    str = u'你好啊！'
    g.name = 'hehe'
    flash(u'你在哪里啊！')
    list1 = [1,2,3,4,5,6,7,8]
    my_int = 10
    my_dict = {
        'name':'zhuo',
        'age': '18'
    }
    context = {
        'list1':list1,
        'my_int':my_int,
        'my_dict':my_dict,
        'str':str,
    }
    return render_template('index.html', **context)

@app.route('/order/<order_id>')
def order(order_id):
    return u'你好啊！'

if __name__ == '__main__':
    app.run()