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


def create_model_obj(model_class, **kwargs):
    add_obj = model_class(
        **kwargs
    )
    db.session.add(add_obj)


def delete_objs(model_class, ids):
    # db.session.query(model_class).filter(model_class.id.in_(ids)).delete(synchronize_session=False)
    objs = model_class.query.filter(model_class.id.in_(ids))
    db.session.delete(objs)


def update_model_obj(model_class, **kwargs):
    id = kwargs.get('id')
    model_obj = model_class.query.filter_by(id=id).first()
    for k, v in kwargs.items():
        setattr(model_obj, k, v)


def get_info(model_class, model_schema, id):
    model_obj = model_class.query.filter_by(id=id).first()
    schema = model_schema()
    result = schema.dump(model_obj)
    return result


def get_infos(model_class, model_schema, **kwargs):
    model_objs = model_class.query.filter_by(**kwargs)
    schema = model_schema(many=True)
    result = schema.dump(model_objs)
    return result


