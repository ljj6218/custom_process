from sqlalchemy import select
from models import *
from app import db
import uuid
session = db.session
from flask import request, jsonify


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
