from app import app, login_manager, db, mongo_db
from views import *
import settings


@login_manager.user_loader
def get_user(id):
    return SysUser.query.get(int(id))


# 首页
@app.route('/')
def index():
    return index_view()


# 用户  注册
@app.route('/register', methods=('GET', 'POST'))  # 登录
def register():
    return register_view()


# 用户  登录
@app.route('/login/', methods=('GET', 'POST'))  # 登录
def login():
    return login_view()


# 用户  登出
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# 人  增
@app.route('/user', methods=['POST'])
def add_user():
    return add_user_view()


# 人  删  单个或多个
@app.route('/users', methods=['DELETE'])
def delete_users():
    return delete_users_view()


# 人  改
@app.route('/user', methods=['PUT'])
def update_user():
    return update_user_view()


# 人  查  单个对象的详情
@app.route('/user', methods=['GET'])
def get_user():
    # obj = mongo_db.connection["custom_process"]
    # for i in dir(obj):
    #     print("- " * 30)
    #     print(i)
    #     try:
    #         print(getattr(obj, i))
    #     except Exception as e:
    #         print(e)
    #         try:
    #             print(getattr(obj, i)())
    #         except Exception as e:
    #             print(e)
    # print()
    # mongo_db.connection.custom_process.insert_one({"key1": "value1", "key2": "value2"})
    # mongo_db.connection.custom_process.insert_one({"key1": "value1", "key2": "value2"})
    from models_mongo import SysUserMongo, MachineMongo
    import datetime
    print(" -"*30)
    print(SysUserMongo._get_collection())
    print(MachineMongo._get_collection())
    u = SysUserMongo._get_collection().insert_one({"key1": "value1", "key2": "value2"})
    print(" -"*30)
    # u = SysUserMongo(sql_id=10086, created_at=datetime.datetime.now())
    # u.aaa = "123"
    # u.save()
    # print(SysUserMongo.objects.all())
    # for i in SysUserMongo.objects.all():
    #     print(i)
    return get_user_view()


# 人  查  列表筛选
@app.route('/users', methods=['GET'])
def get_users():
    return get_users_view()
