FLASK_ADMIN_SWATCH = "cerulean"

SECRET_KEY = "TPmi4aLWRbyVq8zu9v82dWY21"

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://liang:ljj2186@127.0.0.1:3306/custom_process'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# BASIC_AUTH_FORCE = True
# BASIC_AUTH_USERNAME = 'admin'
# BASIC_AUTH_PASSWORD = "123456"

try:
    from local_settings import *
except Exception as e:
    pass
