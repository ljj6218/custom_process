# from app import app
from app import app, login_manager, db
from marshmallows import *
from views import *
import settings
from flask_login import UserMixin  # 引入用户基类
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

# ...
# USERS = [
#     {
#         "id": 1,
#         "name": 'liang',
#         "password": generate_password_hash('123456')
#     },
#     {
#         "id": 2,
#         "name": 'tom',
#         "password": generate_password_hash('123')
#     }
# ]
from werkzeug.security import generate_password_hash
import uuid


# ...
def create_user(username, password):
    """创建一个用户"""
    # user = {
    #     "name": username,
    #     "password": generate_password_hash(password),
    #     "id": uuid.uuid4()
    # }
    # USERS.append(user)
    add_user_view(username=username, password=password)
    db.session.commit()


@login_manager.user_loader
def get_user(id):
    return SysUser.query.get(int(id))


# def get_user(id):
#     """根据用户名获得用户记录"""
#     user_obj = SysUser.query.filter_by(id=id).first()
#     return user_obj
#     # print("user_obj---001")
#     # print(user_obj)
#     # if not user_obj:
#     #     return
#     # sys_users_schema = SysUserSchema()
#     # user_data = sys_users_schema.dump(user_obj)
#     # print(user_data)
#     # return user_data
#     # for user in USERS:
#     #     if user.get("name") == username:
#     #         return user
#     # return None

#
# # ...
# class User(UserMixin):
#     """用户类"""
#
#     def __init__(self, user):
#         self.username = user.get("name")
#         self.password_hash = user.get("password")
#         self.id = user.get("id")
#
#     def verify_password(self, password):
#         """密码验证"""
#         if self.password_hash is None:
#             return False
#         return check_password_hash(self.password_hash, password)
#
#     def get_id(self):
#         """获取用户ID"""
#         return self.id
#
#     @staticmethod
#     def get(user_id):
#         """根据用户ID获取用户实体，为 login_user 方法提供支持"""
#         user_obj = SysUser.query.filter_by(id=user_id).first()
#         if not user_obj:
#             return
#         sys_users_schema = SysUserSchema()
#         user_data = sys_users_schema.dump(user_obj)
#         print(user_data)
#         return user_data
#         # if not user_id:
#         #     return None
#         # for user in USERS:
#         #     if user.get('id') == user_id:
#         #         return User(user)
#         # return None


# @login_manager.user_loader  # 定义获取登录用户的方法
# def load_user(user_id):
#     return SysUser.get(user_id)
    # return db.session.query(SysUser.id == user_id)


from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo
# ...
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    """登录表单类"""
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])


from flask import render_template, redirect, url_for, request
from flask_login import login_user


@app.route('/login/', methods=('GET', 'POST'))  # 登录
def login():
    form = LoginForm()
    emsg = None
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_obj = SysUser.query.filter_by(username=username).first()  # 从用户数据中查找用户记录
        # user_obj = get_user(username)  # 从用户数据中查找用户记录
        # user_info = get_user(username)  # 从用户数据中查找用户记录
        print("user_info----")
        print(username)
        print(password)
        print(user_obj)
        # print(user_info)
        if user_obj is None:
        # if user_info is None:
            emsg = "用户名或密码密码有误"
        else:
            user = user_obj  # 创建用户实体
            # user = SysUser(user_info)  # 创建用户实体
            if user.verify_password(password):  # 校验密码
                print("校验密码成功*----------")
                login_user(user, remember=True)  # 创建用户 Session
                return redirect(request.args.get('next') or url_for('index'))
            else:
                print("校验密码失败*----------")
                emsg = "用户名或密码密码有误"
    return render_template('login.html', form=form, emsg=emsg)


from flask import render_template, url_for
from flask_login import current_user, login_required


# ...
@app.route('/')  # 首页
@login_required  # 需要登录才能访问
def index():
    print("current_user------")
    print(current_user)
    print("current_user------")
    return render_template('index.html', username=current_user.username)


from flask import redirect, url_for
from flask_login import logout_user


# ...
@app.route('/logout')  # 登出
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
