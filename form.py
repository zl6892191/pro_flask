# -*- coding:utf-8 -*-

from flask import Flask,render_template,request,flash
# 创建应用
app = Flask(__name__)
app.config['SECRET_KEY'] = 'jvmw0c-_977ik9obgz1(r$t@q_vi0yk4-$y8rv$mf9dm2la=b3'

# 设置DEBUG 导入模式
app.config.from_pyfile('config.conf')
# 设置路由和视图函数
@app.route('/',methods=['GET','POST'])
def index():
    # 参数校验
    if request.method == 'POST':
        # 获取数据
        username = request.form.get('username')
        pswd1 = request.form.get('pswd1')
        pswd2 = request.form.get('pswd2')
        print username,pswd1,pswd2
        if not all([username,pswd1,pswd2]):
            flash(u'参数不完整!')
        elif pswd1 != pswd2:
            flash(u'两次密码不一样')
        else:
            return u'注册成功！'
    return render_template('form.html')

if __name__ == '__main__':
    app.run()