from sqlalchemy import select
from models import *
from app import db
import uuid
session = db.session
from flask import request, jsonify
from werkzeug.security import generate_password_hash


def add_user_view():
    add_user = SysUser(
        uuid=uuid.uuid4(),
        username="",
        password=generate_password_hash('123456'),
        nick_name="",
        header_img="",
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
