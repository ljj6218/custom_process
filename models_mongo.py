from app import mongo_db


class BaseMongoModel(mongo_db.Document):
    sql_id = mongo_db.IntField(required=True)
    created_at = mongo_db.DateTimeField(required=True)
    updated_at = mongo_db.DateTimeField()
    deleted_at = mongo_db.DateTimeField()

    meta = {'collection': 'base_mongo_model', 'allow_inheritance': True, 'strict': False}


class SysUserMongo(BaseMongoModel):

    meta = {'collection': 'sys_users', 'strict': False}


class MachineMongo(BaseMongoModel):

    meta = {'collection': 'machine', 'strict': False}


class GoodsMongo(BaseMongoModel):

    meta = {'collection': 'goods', 'strict': False}


class EnvironmentMongo(BaseMongoModel):

    meta = {'collection': 'environment', 'strict': False}


class CustomProcessBaseMongo(BaseMongoModel):

    meta = {'collection': 'custom_process_base', 'strict': False}
