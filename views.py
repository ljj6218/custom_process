from sqlalchemy import select
from models import *
from forms import *
from utils import *
from app import db
import uuid
session = db.session
from flask import request, jsonify
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required, login_user, logout_user


def index_view():
    if current_user.is_authenticated:
        return render_template('index.html', username=current_user.username)
    return render_template('index.html', username=None)


# 用户  注册
def register_view():
    form = RegisterForm()

    if not form.validate_on_submit():
        return render_template('register.html', form=form, emsg=None)

    username = form.username.data
    password = form.password.data
    password_2 = form.password_2.data

    if password != password_2:
        return render_template('register.html', form=form, emsg="密码不一致")

    user_obj = SysUser.query.filter_by(username=username).first()  # 从用户数据中查找该用户名

    if user_obj is not None:
        return render_template('register.html', form=form, emsg="用户名已存在")

    create_user(username, password)

    user_obj = SysUser.query.filter_by(username=username).first()  # 从用户数据中查找该用户名
    login_user(user_obj, remember=True)  # 创建用户 Session

    return redirect(request.args.get('next') or url_for('index'))


# 用户登录
def login_view():
    form = LoginForm()

    if not form.validate_on_submit():
        return render_template('register.html', form=form, emsg=None)

    username = form.username.data
    password = form.password.data

    user_obj = SysUser.query.filter_by(username=username).first()  # 从用户数据中查找该用户
    if user_obj is None:
        return render_template('register.html', form=form, emsg="用户名或密码有误")

    if not user_obj.verify_password(password):  # 校验密码
        return render_template('login.html', form=form, emsg="用户名或密码密码有误")

    login_user(user_obj, remember=True)  # 创建用户 Session
    return redirect(request.args.get('next') or url_for('index'))


def deletev_user_view():
    pass
    return jsonify(dict(
        code="0",
        msg="成功",
        data={},
    ))


def update_user_view():
    pass
    return jsonify(dict(
        code="0",
        msg="成功",
        data={},
    ))


def get_user_view():

    return jsonify(dict(
        code="0",
        msg="成功",
        data={},
    ))


def deletev_users_view():
    pass
    return jsonify(dict(
        code="0",
        msg="成功",
        data={},
    ))


def get_users_view():
    pass
    return jsonify(dict(
        code="0",
        msg="成功",
        data={},
    ))
