"""
"""

from flask import Blueprint, request


order_resource = Blueprint("order_resource", "order_resource")

from server.controller.order_controller import OrderController
from server.models.order import Order
from server.exceptions import BanzeeException
from server.api.response_resource import *


order_resource = Blueprint("order_resource", "order_resource")

@order_resource.route("/v1/orders", methods=["GET"])
def get_order_list_by_user_id():
    user_id = None

    q = request.args.get("q", None)
    offset = request.args.get("offset", 0, type=int)
    fetch = request.args.get("fetch", 20, type=int)

    response_status = 200
    order_list = None
    try:
        order_list = OrderController().get_list_by_user_id(user_id, q, offset, fetch)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="orders", body_dict=order_list)


@order_resource.route("/v1/orders/<string:order_id>", methods=["GET"])
def get_order(order_id):
    response_status = 200
    order = None
    try:
        order = OrderController().get(order_id)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="order", body_dict=order)


@order_resource.route("/v1/orders", methods=["POST"])
def create_order():
    response_status = 200
    params = request.get_json()

    order_dict = None
    try:
        order_dict = OrderController().create(
            params["user_id"], 
            params["platform_type"], 
            params["app_type"])

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key="order", body_dict=order_dict)


@order_resource.route("/v1/orders/<string:order_id>", methods=["DELETE"])
def cancel_order(order_id):
    response_status = 200

    try:
        res = OrderController().cancel(order_id)

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key=None, body_dict=None)
