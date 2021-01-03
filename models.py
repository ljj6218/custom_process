# coding: utf-8
from sqlalchemy import func
from app import db
from flask_login import UserMixin  # 引入用户基类
from werkzeug.security import check_password_hash


class BaseModel(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True, comment='id')
    created_at = db.Column(db.DateTime, server_default=func.now(), comment='创建时间')
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), comment='修改时间')
    deleted_at = db.Column(db.DateTime, index=True, comment='删除时间')
    __abstract__ = True


class SysUser(BaseModel, UserMixin):
    __tablename__ = 'sys_users'
    uuid = db.Column(db.String(191), info='用户UUID')
    username = db.Column(db.String(191), info='用户登录名')
    password = db.Column(db.String(191), info='用户登录密码')
    nick_name = db.Column(db.String(191), server_default=db.FetchedValue(), info='用户昵称')
    header_img = db.Column(db.String(191), server_default=db.FetchedValue(), info='用户头像')
    authority_id = db.Column(db.String(90), server_default=db.FetchedValue(), info='用户角色ID')

    # def __init__(self, user):
    #     self.username = user.get("name")
    #     self.password_hash = user.get("password")
    #     self.id = user.get("id")

    def verify_password(self, password):
        """密码验证"""
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    # def get_id(self):
    #     """获取用户ID"""
    #     return self.id

    # @staticmethod
    # def get(user_id):
    #     """根据用户ID获取用户实体，为 login_user 方法提供支持"""
    #     user_obj = SysUser.query.filter_by(id=user_id).first()
    #     if not user_obj:
    #         return
    #     from marshmallows import SysUserSchema
    #     sys_users_schema = SysUserSchema()
    #     user_data = sys_users_schema.dump(user_obj)
    #     print(user_data)
    #     return user_data
    #     # if not user_id:
    #     #     return None
    #     # for user in USERS:
    #     #     if user.get('id') == user_id:
    #     #         return User(user)
    #     # return None


class Machine(BaseModel):
    __tablename__ = 'machine'
    name = db.Column(db.String(64), info='名称')


class Good(BaseModel):
    __tablename__ = 'goods'
    name = db.Column(db.String(64), info='名称')


class Environment(BaseModel):
    __tablename__ = 'environment'
    name = db.Column(db.String(64), info='名称')


class CustomProcessBase(BaseModel):
    __tablename__ = 'custom_process_base'
    name = db.Column(db.String(64), info='名称')
    from_url = db.Column(db.String(512), info='来源')
    to_url = db.Column(db.String(512), info='去向')


class CustomProcessBaseUserRel(BaseModel):
    __tablename__ = 'custom_process_base_user_rel'
    base_id = db.Column(db.BigInteger)
    user_id = db.Column(db.BigInteger)


class CustomProcessBaseMachineRel(BaseModel):
    __tablename__ = 'custom_process_base_machine_rel'
    base_id = db.Column(db.BigInteger)
    machine_id = db.Column(db.BigInteger)


class CustomProcessBaseGoodsRel(BaseModel):
    __tablename__ = 'custom_process_base_goods_rel'
    base_id = db.Column(db.BigInteger)
    goods_id = db.Column(db.BigInteger)


class CustomProcessBaseEnvironmentRel(BaseModel):
    __tablename__ = 'custom_process_base_environment_rel'
    environment_id = db.Column(db.BigInteger)
    base_id = db.Column(db.BigInteger)


class Template(BaseModel):
    __tablename__ = 'template'
    name = db.Column(db.String(64))


class IdCard(BaseModel):
    __tablename__ = 'id_card'
    type = db.Column(db.Integer, info='类型')
    id1 = db.Column(db.String(8))
    id2 = db.Column(db.String(8))
    id3 = db.Column(db.String(8))
    id4 = db.Column(db.String(8))
    id5 = db.Column(db.String(8))
    id6 = db.Column(db.String(8))
    id7 = db.Column(db.String(8))
    id8 = db.Column(db.String(8))


class IdCardDecode(BaseModel):
    __tablename__ = 'id_card_decode'
    name = db.Column(db.String(64))


class SysOperationRecord(BaseModel):
    __tablename__ = 'sys_operation_records'
    ip = db.Column(db.String(191), info='请求ip')
    method = db.Column(db.String(191), info='请求方法')
    path = db.Column(db.String(191), info='请求路径')
    status = db.Column(db.BigInteger, info='请求状态')
    latency = db.Column(db.BigInteger, info='延迟')
    agent = db.Column(db.String(191), info='代理')
    error_message = db.Column(db.String(191), info='错误信息')
    body = db.Column(db.String, info='请求Body')
    resp = db.Column(db.String, info='响应Body')
    user_id = db.Column(db.BigInteger, info='用户id')
