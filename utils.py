from app import db
import traceback
from models import *
session = db.session


def affair_decorator(a_func):
    def wrap_the_function():
        print("I am doing some boring work before executing view()")
        try:
            a_func()
        except:
            traceback.print_exc()
            session.rollback()
            raise
        else:
            session.commit()

        print("I am doing some boring work after executing view()")

    return wrap_the_function


def create_user(username, password):
    """创建一个用户"""
    SysUser.add_user_view(username=username, password=password)
    db.session.commit()
