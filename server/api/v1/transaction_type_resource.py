"""
"""

from flask import Blueprint, request

from server.controller.transaction_type_controller import TransactionTypeController
from server.models.transaction_type import TransactionType
from server.exceptions import BanzeeException
from server.api.response_resource import *


transaction_type_resource = Blueprint("transaction_type_resource", "transaction_type_resource")

@transaction_type_resource.route("/v1/transaction_types", methods=["GET"])
def get_transaction_type_list():
    q = request.args.get("q", None)
    offset = request.args.get("offset", 0, type=int)
    fetch = request.args.get("fetch", 20, type=int)

    response_status = 200
    type_list = None
    try:
        type_list = TransactionTypeController().get_list(q, offset, fetch)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="transaction_types", body_dict=type_list)


@transaction_type_resource.route("/v1/transaction_types/<string:trx_type>", methods=["GET"])
def get_transaction_type(trx_type):
    response_status = 200
    type_dict = None
    try:
        type_dict = TransactionTypeController().get(trx_type)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="transaction_type", body_dict=type_dict)


@transaction_type_resource.route("/v1/transaction_types", methods=["POST"])
def create_transaction_type():
    response_status = 200
    params = request.get_json()

    type_dict = None
    try:
        transactionType = TransactionType(params["trx_type"], params["trx_type_name"], params["io_type"], params["trx_type_description"])
        type_dict = TransactionTypeController().create(transactionType)

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key="transaction_type", body_dict=type_dict)


@transaction_type_resource.route("/v1/transaction_types/<string:trx_type>", methods=["PUT"])
def update_transaction_type(trx_type):
    response_status = 200
    params = request.get_json()

    type_dict = None
    try:
        transactionType = TransactionType(trx_type, params["trx_type_name"], params["trx_type_description"])
        type_dict = TransactionTypeController().update(transactionType)

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key="transaction_type", body_dict=type_dict)


@transaction_type_resource.route("/v1/transaction_types/<string:trx_type>", methods=["DELETE"])
def delete_transaction_type(trx_type):
    response_status = 200

    try:
        res = TransactionTypeController().delete(trx_type)

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key=None, body_dict=None)
