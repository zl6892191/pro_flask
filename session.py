# -*- coding:utf-8 -*-

from flask import Flask,session
# 创建应用
app = Flask(__name__)
# 设置加密密钥
app.config['SECRET_KEY'] = 'jvmw0c-_977ik9obgz1(r$t@q_vi0yk4-$y8rv$mf9dm2la=b3'
# 设置DEBUG 导入模式
app.config.from_pyfile('config.conf')
# 设置session
@app.route('/index')
def index():
    # 设置session
    session.permanent = True
    session['name'] = 'zhuolin'
    return '设置session成功！'
# 获取session
@app.route('/get_session')
def demo():
    name = session['name']
    return name

# 删除session
@app.route('/del_session')
def zux():
    session.pop('name')
    return '删除成功！'
if __name__ == '__main__':
    app.run()