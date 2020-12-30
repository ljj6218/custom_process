# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)


class CustomProcessBase(BaseModel):
    __tablename__ = 'custom_process_base'
    name = db.Column(db.String(64), info='名称')
    from_url = db.Column(db.String(512), info='来源')
    to_url = db.Column(db.String(512), info='去向')


class CustomProcessBaseEnvironmentRel(BaseModel):
    __tablename__ = 'custom_process_base_environment_rel'
    environment_id = db.Column(db.BigInteger)
    base_id = db.Column(db.BigInteger)


class CustomProcessBaseGoodsRel(BaseModel):
    __tablename__ = 'custom_process_base_goods_rel'
    base_id = db.Column(db.BigInteger)
    goods_id = db.Column(db.BigInteger)


class CustomProcessBaseMachineRel(BaseModel):
    __tablename__ = 'custom_process_base_machine_rel'
    base_id = db.Column(db.BigInteger)
    machine_id = db.Column(db.BigInteger)


class CustomProcessBaseUserRel(BaseModel):
    __tablename__ = 'custom_process_base_user_rel'
    base_id = db.Column(db.BigInteger)
    user_id = db.Column(db.BigInteger)


class Environment(BaseModel):
    __tablename__ = 'environment'
    name = db.Column(db.String(64), info='名称')


class Good(BaseModel):
    __tablename__ = 'goods'
    name = db.Column(db.String(64), info='名称')


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


class Machine(BaseModel):
    __tablename__ = 'machine'
    name = db.Column(db.String(64), info='名称')


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


class SysUser(BaseModel):
    __tablename__ = 'sys_users'
    uuid = db.Column(db.String(191), info='用户UUID')
    username = db.Column(db.String(191), info='用户登录名')
    password = db.Column(db.String(191), info='用户登录密码')
    nick_name = db.Column(db.String(191), server_default=db.FetchedValue(), info='用户昵称')
    header_img = db.Column(db.String(191), server_default=db.FetchedValue(), info='用户头像')
    authority_id = db.Column(db.String(90), server_default=db.FetchedValue(), info='用户角色ID')


class Template(BaseModel):
    __tablename__ = 'template'
    name = db.Column(db.String(64))
