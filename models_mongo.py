from app import mongo_db


class BaseMongoModel(object):
    sql_id = mongo_db.IntField(required=True)


class SysUserMongo(BaseMongoModel, mongo_db.Document):

    meta = {'collection': 'sys_users', 'strict': False}


class MachineMongo(BaseMongoModel, mongo_db.Document):

    meta = {'collection': 'machine', 'strict': False}


class GoodsMongo(BaseMongoModel, mongo_db.Document):

    meta = {'collection': 'goods', 'strict': False}


class EnvironmentMongo(BaseMongoModel, mongo_db.Document):

    meta = {'collection': 'environment', 'strict': False}


class CustomProcessBaseMongo(BaseMongoModel, mongo_db.Document):

    meta = {'collection': 'custom_process_base', 'strict': False}
