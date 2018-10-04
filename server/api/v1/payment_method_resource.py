"""
"""

from flask import Blueprint, request

from server.controller.payment_method_controller import PaymentMethodController
from server.models.payment_method import PaymentMethod
from server.exceptions import BanzeeException
from server.api.response_resource import *


payment_method_resource = Blueprint("payment_method_resource", "payment_method_resource")

@payment_method_resource.route("/v1/payment_methods", methods=["GET"])
def get_payment_method_list():
    q = request.args.get("q", None)
    offset = request.args.get("offset", 0, type=int)
    fetch = request.args.get("fetch", 20, type=int)

    response_status = 200
    try:
        method_list = PaymentMethodController().get_list(q, offset, fetch)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="payment_methods", body_dict=method_list)


@payment_method_resource.route("/v1/payment_methods/<string:method_code>", methods=["GET"])
def get_payment_method(method_code):
    response_status = 200
    try:
        method_dict = PaymentMethodController().get(method_code)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="payment_method", body_dict=method_dict)


@payment_method_resource.route("/v1/payment_methods", methods=["POST"])
def create_payment_method():
    response_status = 200
    params = request.get_json()

    method_dict = None
    try:
        paymentMethod = PaymentMethod(params["method_code"], params["method_status"], params["method_name"], params["method_type"])
        method_dict = PaymentMethodController().create(paymentMethod)

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key="payment_method", body_dict=method_dict)


@payment_method_resource.route("/v1/payment_methods/<string:method_code>", methods=["PUT"])
def update_payment_method(method_code):
    response_status = 200
    params = request.get_json()

    method_dict = None
    try:
        paymentMethod = PaymentMethod(params["method_code"], params["method_status"], params["method_name"], params["method_type"])
        method_dict = PaymentMethodController().update(paymentMethod)

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key="payment_method", body_dict=method_dict)


@payment_method_resource.route("/v1/partners/<string:method_code>", methods=["DELETE"])
def delete_payment_method(method_code):
    response_status = 200

    try:
        res = PaymentMethodController().delete(method_code)

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key=None, body_dict=None)
