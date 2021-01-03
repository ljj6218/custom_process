from app import app, login_manager, db
from marshmallows import *
from utils import *
from views import *
import settings

from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required, login_user, logout_user
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo


@login_manager.user_loader
def get_user(id):
    return SysUser.query.get(int(id))


class RegisterForm(FlaskForm):
    """登录表单类"""
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    password_2 = PasswordField('重复密码', validators=[DataRequired()])


class LoginForm(FlaskForm):
    """登录表单类"""
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])


# 用户  注册
@app.route('/register', methods=('GET', 'POST'))  # 登录
def register():
    form = RegisterForm()

    if not form.validate_on_submit():
        return render_template('login.html', form=form, emsg=None)

    username = form.username.data
    password = form.password.data
    password_2 = form.password_2.data

    if password != password_2:
        return render_template('login.html', form=form, emsg="用户名或密码密码有误")

    user_obj = SysUser.query.filter_by(username=username).first()  # 从用户数据中查找该用户名

    if user_obj is not None:
        return render_template('login.html', form=form, emsg="用户名已存在")

    create_user(username, password)
    return redirect(request.args.get('next') or url_for('index'))


# 用户登录
@app.route('/login/', methods=('GET', 'POST'))  # 登录
def login():
    form = LoginForm()
    emsg = None
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_obj = SysUser.query.filter_by(username=username).first()  # 从用户数据中查找该用户
        if user_obj is None:
            emsg = "用户名或密码密码有误"
        if user_obj.verify_password(password):  # 校验密码
            print("校验密码成功*----------")
            login_user(user_obj, remember=True)  # 创建用户 Session
            return redirect(request.args.get('next') or url_for('index'))
        else:
            print("校验密码失败*----------")
            emsg = "用户名或密码密码有误"
    return render_template('login.html', form=form, emsg=emsg)


# 首页
@app.route('/')
def index():
    return render_template('index.html', username=current_user.username)


# 登出
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# @app.route('/')
# def hello_world():
#     print(settings.AAA)
#     return 'Hello World'
#
#
# @app.route('/user', methods=['POST'])
# def add_user():
#     return add_user_view()
#
#
# @app.route('/user', methods=['DELETE'])
# def delete_user():
#     return deletev_user_view()
#
#
# @app.route('/user', methods=['PUT'])
# def update_user():
#     return update_user_view()
#
#
# @app.route('/user', methods=['GET'])
# def get_user():
#     return get_user_view()
#
#
# @app.route('/users', methods=['DELETE'])
# def delete_users():
#     return deletev_users_view()
#
#
# @app.route('/users', methods=['GET'])
# def get_users():
#     return get_users_view()
