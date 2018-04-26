# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# 创建应用
app = Flask(__name__)
# 设置DEBUG 导入模式
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test1:666666@192.168.44.160:3306/flask_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('config.conf')
# 链接数据库,创建数据库对象
db = SQLAlchemy(app)
# 设置连接数据库
# 设置角色模型类
class Role(db.Model):
    __tablename__ = 'roles'
    # 用户ID（主键）
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True)

    def __repr__(self):
        return '<Role:%s>'%self.name

# 设置用户模型类
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(63),unique=True)
    role_id = db.Column(db.Integer,db.ForeignKey(Role.id))

    def __repr__(self):
        return '<User:%s>'%self.name

# 设置路由和视图函数
@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    # 生成表
    db.drop_all()
    db.create_all()
    app.run()