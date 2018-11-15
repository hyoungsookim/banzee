"""
"""

from flask import Blueprint, request

from server.controller.account_type_controller import AccountTypeController
from server.models.account_type import AccountType
from server.exceptions import BanzeeException
from server.api.response_resource import *


account_type_resource = Blueprint("account_type_resource", "account_type_resource")

@account_type_resource.route("/v1/account_types", methods=["GET"])
def get_account_type_list():
    q = request.args.get("q", None)
    offset = request.args.get("offset", 0, type=int)
    fetch = request.args.get("fetch", 20, type=int)

    response_status = 200
    type_list = None
    try:
        type_list = AccountTypeController().get_list(q, offset, fetch)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="account_types", body_dict=type_list)


@account_type_resource.route("/v1/account_types/<string:account_type>", methods=["GET"])
def get_account_type(account_type):
    response_status = 200
    type_dict = None
    try:
        type_dict = AccountTypeController().get(account_type)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="account_type", body_dict=type_dict)


@account_type_resource.route("/v1/account_types", methods=["POST"])
def create_account_type():
    response_status = 200
    params = request.get_json()

    type_dict = None
    try:
        accountType = AccountType(
                        params["account_type"], 
                        params["account_type_name"], 
                        params["account_type_status"], 
                        params.get("account_type_description", None)
        )
        type_dict = AccountTypeController().create(accountType)

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key="account_type", body_dict=type_dict)


@account_type_resource.route("/v1/account_types/<string:account_type>", methods=["PUT"])
def update_account_type(account_type):
    response_status = 200
    params = request.get_json()

    type_dict = None
    try:
        accountType = AccountType(
                            account_type, 
                            params["account_type_name"], 
                            params["account_type_status"], 
                            params.get("account_type_description", None)
        )

        type_dict = AccountTypeController().update(accountType)

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key="account_type", body_dict=type_dict)


@account_type_resource.route("/v1/account_types/<string:account_type>", methods=["DELETE"])
def delete_account_type(account_type):
    response_status = 200

    try:
        res = AccountTypeController().delete(account_type)

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key=None, body_dict=None)
