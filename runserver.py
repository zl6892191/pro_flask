# -*- coding:utf-8 -*-

from flask import Flask
from flask_script import Manager

# 创建应用
app = Flask(__name__)
# 实例化脚本管理器
manager = Manager(app)
# 设置DEBUG 导入模式
app.config.from_pyfile('config.conf')
# 设置路由和视图函数
@app.route('/')
def index():
    a = 10/0
    return 'hello world'

if __name__ == '__main__':
    manager.run()