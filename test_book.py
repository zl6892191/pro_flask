# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request,render_template,flash
# 创建应用
app = Flask(__name__)
# 链接数据库
# 设置DEBUG 导入模式
app.config.from_pyfile('config.conf')
app.config['SECRET_KEY'] = 'jvmw0c-_977ik9obgz1(r$t@q_vi0yk4-$y8rv$mf9dm2la=b3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test1:666666@192.168.44.160:3306/flask_test_book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 创建数据库对象
db = SQLAlchemy(app)
# 添加两个类
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    au_book = db.relationship('Book',backref='Author',lazy = True)
    def __repr__(self):
        return u'作者:%s' %self.name

#定义模型类-书名
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    au_bookid = db.Column(db.Integer,db.ForeignKey('author.id'))
    def __str__(self):
        return u'书名:%s'%(self.name)
# 设置路由和视图函数
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        bookname = request.form.get('bookname')
        # 判断作者是否存在
        a = Author.query.filter(Author.name==username).first()
        if a:
            print '---1---'
            if Book.query.filter(Book.name == bookname,Book.au_bookid==a.id).first():
                print '---2---'
                flash(u'作者喝书名已存在')
            else:
                # 添加书名,绑定给作者
                try:

                    book1 = Book(name=bookname,au_bookid = a.id)
                    db.session.add(book1)
                    db.session.commit()
                except Exception as e:
                    print e
                    db.session.rollback()
        else:
            # 添加作者和添加书名字
            try:
                author1 = Author(name=username)
                db.session.add(author1)
                db.session.commit()
                book2 = Book(name=bookname, au_bookid = author1.id)
                db.session.add(book2)
                db.session.commit()
            except Exception as e:
                print e

    author = Author.query.all()
    books = Book.query.all()
    return render_template('flask_book.html', author=author, books=books)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    au1 = Author(name='老王')
    au2 = Author(name='老尹')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()
    bk1 = Book(name='老王回忆录', au_bookid=au1.id)
    bk2 = Book(name='我读书少，你别骗我', au_bookid=au1.id)
    bk3 = Book(name='如何才能让自己更骚', au_bookid=au2.id)
    bk4 = Book(name='怎样征服美丽少女', au_bookid=au3.id)
    bk5 = Book(name='如何征服英俊少男', au_bookid=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()
    app.run()