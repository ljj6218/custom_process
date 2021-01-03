from flask import Flask
import settings
from flask_sqlalchemy import SQLAlchemy
from flask_basicauth import BasicAuth
import flask_login
from flask_login import LoginManager

app = Flask(__name__)

# 加载配置
app.config.from_object(settings)

# 创建数据库连接
db = SQLAlchemy(app)

basic_auth = BasicAuth(app)

# login_manager = LoginManager()  # 实例化登录管理对象
# login_manager.init_app(app)  # 初始化应用
# login_manager.login_view = 'login'  # 设置用户登录视图函数 endpoint

# 注册admin、中间件
from register import *

# 注册urls
from urls import *


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
