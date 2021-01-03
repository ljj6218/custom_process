from sqlalchemy import select
from models import *
from app import db
import uuid
session = db.session
from flask import request, jsonify
from werkzeug.security import generate_password_hash


def add_user_view(**kwargs):
    add_user = SysUser(
        uuid=str(uuid.uuid4()),
        username=kwargs.get('username'),
        password=generate_password_hash(kwargs.get('password')),
        nick_name=kwargs.get('nick_name'),
        header_img=kwargs.get('header_img'),
        authority_id="",
    )
    session.add(add_user)
    # session.commit()
    return jsonify(dict(
        code="1",
        msg="成功",
        data={},
    ))


def deletev_user_view():
    pass
    return jsonify(dict(
        code="0",
        msg="成功",
        data={},
    ))


def update_user_view():
    pass
    return jsonify(dict(
        code="0",
        msg="成功",
        data={},
    ))


def get_user_view():

    return jsonify(dict(
        code="0",
        msg="成功",
        data={},
    ))


def deletev_users_view():
    pass
    return jsonify(dict(
        code="0",
        msg="成功",
        data={},
    ))


def get_users_view():
    pass
    return jsonify(dict(
        code="0",
        msg="成功",
        data={},
    ))
