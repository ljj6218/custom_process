from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import request

from app import app, db
from models import *

admin = Admin(app, name='custom_process', template_mode='bootstrap3')


class BaseModelView(ModelView):
    column_searchable_list = ['id', 'created_at', 'updated_at', 'deleted_at']


class SysUserModelView(BaseModelView):
    column_searchable_list = ['id', 'created_at', 'updated_at', 'deleted_at', 'username', 'nick_name']


class FileterNameModelView(ModelView):
    column_searchable_list = ['id', 'created_at', 'updated_at', 'deleted_at', 'name', ]


class CustomProcessBaseModelView(ModelView):
    column_searchable_list = ['id', 'created_at', 'updated_at', 'deleted_at', 'name', 'from_url', 'to_url']


class CustomProcessBaseUserRelModelView(ModelView):
    column_searchable_list = ['base_id', 'user_id']


class CustomProcessBaseMachineRelModelView(ModelView):
    column_searchable_list = ['base_id', 'machine_id']


class CustomProcessBaseGoodsRelModelView(ModelView):
    column_searchable_list = ['base_id', 'goods_id']


class CustomProcessBaseEnvironmentRelModelView(ModelView):
    column_searchable_list = ['base_id', 'environment_id']


class IdCardModelView(ModelView):
    column_searchable_list = ['type', 'id1', 'id2', 'id3', 'id4', 'id5', 'id6', 'id7', 'id8']


class SysOperationRecordModelView(ModelView):
    column_searchable_list = ['ip', 'method', 'path', 'status', 'latency', 'agent', 'error_message', 'body', 'resp',
                              'user_id']


# Add administrative views herev
admin.add_view(SysUserModelView(SysUser, db.session))
admin.add_view(FileterNameModelView(Machine, db.session))
admin.add_view(FileterNameModelView(Good, db.session))
admin.add_view(FileterNameModelView(Environment, db.session))
admin.add_view(CustomProcessBaseModelView(CustomProcessBase, db.session))
admin.add_view(CustomProcessBaseUserRelModelView(CustomProcessBaseUserRel, db.session))
admin.add_view(CustomProcessBaseMachineRelModelView(CustomProcessBaseMachineRel, db.session))
admin.add_view(CustomProcessBaseGoodsRelModelView(CustomProcessBaseGoodsRel, db.session))
admin.add_view(CustomProcessBaseEnvironmentRelModelView(CustomProcessBaseEnvironmentRel, db.session))
admin.add_view(IdCardModelView(IdCard, db.session))
admin.add_view(FileterNameModelView(IdCardDecode, db.session))
admin.add_view(FileterNameModelView(Template, db.session))
admin.add_view(SysOperationRecordModelView(SysOperationRecord, db.session))


@app.before_request
def process():
    # print(request.method)
    # request.name = 'pdun'
    # print('请求来的时候')
    pass


@app.after_request
def text(response):  # 需要带参数
    print(request.method)
    print(response)
    print(response.is_json)
    if request.method == "POST" and response.is_json:
        json_content = response.get_json()
        print(json_content)
        if json_content.get('code') != "0":
            print('rollback')
            db.session.rollback()
        else:
            db.session.commit()
        print("002")
    # print('text----', request.name)
    # print('请求走的时候')
    return response  # 需要返回出去
