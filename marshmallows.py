from marshmallow import Schema, fields


class BaseSchema(Schema):
    id = fields.Int()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()


class SysUserSchema(BaseSchema):
    uuid = fields.UUID()
    username = fields.Str()
    password = fields.Str()
    nick_name = fields.Str()
    header_img = fields.Str()
    authority_id = fields.Str()
# from pprint import pprint
#
# user = User(name="Monty", email="monty@python.org")
# schema = UserSchema()
# result = schema.dump(user)
# pprint(result)

# user_data = {
#     "created_at": "2014-08-11T05:26:03.869245",
#     "email": "ken@yahoo.com",
#     "name": "Ken",
# }
# schema = UserSchema()
# result = schema.load(user_data)
# pprint(result)