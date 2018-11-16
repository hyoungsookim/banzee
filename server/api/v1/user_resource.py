"""
"""

from flask import Blueprint, request

from server.controller.user_controller import UserController
from server.models.user import User
from server.exceptions import BanzeeException
from server.api.response_resource import *


user_resource = Blueprint("user_resource", "user_resource")

@user_resource.route("/v1/users", methods=["GET"])
def get_user_list():
    q = request.args.get("q", None)
    offset = request.args.get("offset", 0, type=int)
    fetch = request.args.get("fetch", 20, type=int)

    response_status = 200
    user_list = None
    try:
        user_list = UserController().get_list(q, offset, fetch)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="users", body_dict=user_list)


@user_resource.route("/v1/users/<string:user_id>", methods=["GET"])
def get_user(user_id):
    response_status = 200
    user = None
    try:
        user = UserController().get(user_id)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="user", body_dict=user)


@user_resource.route("/v1/users", methods=["POST"])
def create_user():
    response_status = 200
    params = request.get_json()

    user_dict = None
    try:
        user = User(params["user_id"], 
                    params["partner_id"], 
                    200, 
                    1, 
                    1, 
                    params["first_name"], 
                    params["last_name"])
        user_dict = UserController().create(user)

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key="user", body_dict=user_dict)


@user_resource.route("/v1/users/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    response_status = 200
    params = request.get_json()

    user_dict = None
    try:
        user = User(user_id, 
                    None, 
                    params["user_status"], 
                    params["user_type"], 
                    params["user_level"], 
                    params["first_name"], 
                    params["last_name"])
        user_dict = UserController().update(user)

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key="user", body_dict=user_dict)


@user_resource.route("/v1/users/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    response_status = 200

    try:
        res = UserController().delete(user_id)

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key=None, body_dict=None)


@user_resource.route("/v1/users/<string:user_id>/accounts", methods=["GET"])
def get_account_list(user_id):
    q = request.args.get("q", None)
    offset = request.args.get("offset", 0, type=int)
    fetch = request.args.get("fetch", 20, type=int)

    response_status = 200
    account_list = None
    try:
        account_list = UserController().get_account_list(user_id)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="accounts", body_dict=account_list)


@user_resource.route("/v1/users/<string:user_id>/accounts/<string:account_id>", methods=["GET"])
def get_account(user_id, account_id):
    response_status = 200
    account = None
    try:
        account = UserController().get_account(user_id, account_id)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="account", body_dict=account)


@user_resource.route("/v1/users/<string:user_id>/accounts", methods=["POST"])
def open_account(user_id):
    response_status = 200
    params = request.get_json()

    account = None
    try:
        account = UserController().open_account(user_id, params["account_type"])

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key="account", body_dict=account)


@user_resource.route("/v1/users/<string:user_id>/accounts/<string:account_id>", methods=["DELETE"])
def close_account(user_id, account_id):
    response_status = 200

    account_dict = None
    try:
        account_dict = UserController().close_account(user_id, account_id)

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key=None, body_dict=None)


@user_resource.route("/v1/users/<string:user_id>/accounts/<string:account_id>", methods=["PUT"])
def change_account_status():
    response_status = 200
    params = request.get_json()

    new_status = params["new_status"]
    
    account_dict = None
    try:
        account_dict = UserController().close_account(user_id, account_type, new_status)

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key=None, body_dict=None)


@user_resource.route("/v1/users/<string:user_id>/accounts/<string:account_id>/transactions", methods=["GET"])
def get_transaction_list(user_id, account_id):
    q = request.args.get("q", None)
    offset = request.args.get("offset", 0, type=int)
    fetch = request.args.get("fetch", 20, type=int)

    response_status = 200
    trx_list = None
    try:
        trx_list = UserController().get_transaction_list(account_id)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="transactions", body_dict=trx_list)
