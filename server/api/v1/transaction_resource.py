"""
"""

from flask import Blueprint, request
from server.controller.transaction_controller import TransactionController
from server.models.transaction import Transaction
from server.exceptions import BanzeeException
from server.api.response_resource import *


transaction_resource = Blueprint("transaction_resource", "transaction_resource")

@transaction_resource.route("/v1/transactions", methods=["GET"])
def get_transaction_list():
    q = request.args.get("q", None)
    offset = request.args.get("offset", 0, type=int)
    fetch = request.args.get("fetch", 20, type=int)

    response_status = 200
    transactioin_list = None
    try:
        transaction_list = TransactionController().get_list(None, q, offset, fetch)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="transactions", body_dict=transaction_list)


@transaction_resource.route("/v1/transactions/<string:trx_id>", methods=["GET"])
def get_transaction(trx_id):
    response_status = 200
    transaction_dict = None
    try:
        transaction_dict = TransactionController().get(trx_id)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="transaction", body_dict=transaction_dict)


@transaction_resource.route("/v1/transactions", methods=["POST"])
def deposit_fund():
    response_status = 200
    params = request.get_json()

    transaction_dict = None
    try:
        sender_id = params["sender_id"]
        recipient_account_id = params["recipient_account_id"]
        deposit_type = params["deposit_type"]
        deposit_amount = params["deposit_amount"]
        reason = params.get("reason", None)

        transaction_dict = TransactionController().deposit_fund(
                                                        sender_id,
                                                        recipient_account_id,
                                                        deposit_type,
                                                        deposit_amount,
                                                        reason
        )

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key="transaction", body_dict=transaction_dict)


@transaction_resource.route("/v1/transactions", methods=["DELETE"])
def withdraw_fund():
    response_status = 200
    params = request.get_json()

    transaction_dict = None
    try:
        account_id = params["account_id"]
        withdrawal_amount = params["withdrawal_amount"]
        source_transaction_id = params["source_transaction_id"]
        reason = params.get("reason", None)

        transaction_dict = TransactionController().withdraw_fund(
                                                        account_id,
                                                        withdrawal_amount,
                                                        source_transaction_id,
                                                        reason
        )

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key=None, body_dict=None)
