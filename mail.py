# -*- coding:utf-8 -*-
from flask_mail import Mail,Message
from flask import Flask,render_template
# 创建应用
app = Flask(__name__)
# 设置DEBUG 导入模式
app.config['MAIL_SERVER'] = "smtp.163.net"
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '13922121005@163.com'
app.config['MAIL_PASSWORD'] = 'zl6892191'
app.config['MAIL_DEFAULT_SENDER'] = 'python<13922121005@163.com>'
# 和应用建立关联
mail = Mail(app)
message = Message()
message.subject = '我是邮件标题'
message.recipients = ['zhangjiesharp@163.com']
# message.body= '我是邮件正⽂ text'
message.html = '<h1>我是HTML邮件正⽂</h1>'
mail.send(message)
# 设置路由和视图函数
# 设置DEBUG 导入模式
app.config.from_pyfile('config.conf')
# 设置路由和视图函数
@app.route('/aaaaa')
def index():
    return '正在发送中！！！'

if __name__ == '__main__':
    app.run()