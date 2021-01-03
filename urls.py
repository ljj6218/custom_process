from app import app, login_manager, db
from views import *
import settings


@login_manager.user_loader
def get_user(id):
    return SysUser.query.get(int(id))


# 用户  注册
@app.route('/register', methods=('GET', 'POST'))  # 登录
def register():
    return register_view()


# 用户登录
@app.route('/login/', methods=('GET', 'POST'))  # 登录
def login():
    return login_view()


# 首页
@app.route('/')
def index():
    return index_view()


# 登出
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

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
