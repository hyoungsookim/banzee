"""
"""

from flask import Blueprint, request

from server.controller.payment_method_controller import PaymentMethodController
from server.api.response_resource import *
from server.models.payment_method import PaymentMethod


payment_method_resource = Blueprint("payment_method_resource", "payment_method_resource")

@payment_method_resource.route("/v1/payment_methods", methods=["GET"])
def get_partner_list():
    q = request.args.get("q", None)
    offset = request.args.get("offset", 0, type=int)
    fetch = request.args.get("fetch", 20, type=int)

    response_status = 200
    try:
        method_list = PaymentMethodController().get_list(q, offset, fetch)
    except:
        raise
    
    return create_json_response(response_status, query_dict=None, body_key="payment_methods", body_dict=method_list)


@payment_method_resource.route("/v1/payment_methods/<string:partner_id>", methods=["GET"])
def get_partner(partner_id):
    response_status = 200
    try:
        partner = PaymentMethodController().get(partner_id)
    except:
        raise
    
    return create_json_response(response_status, query_dict=None, body_key="payment_method", body_dict=partner)
