"""
"""

from flask import Blueprint, request

from server.controller.partner_controller import PartnerController
from server.api.response_resource import *
from server.models.partner import Partner


partner_resource = Blueprint("partner_resource", "partner_resource")

@partner_resource.route("/v1/partners", methods=["GET"])
def get_partner_list():
    q = request.args.get("q", None)
    offset = request.args.get("offset", 0, type=int)
    fetch = request.args.get("fetch", 20, type=int)

    response_status = 200
    try:
        partner_list = PartnerController().get_list(q, offset, fetch)
    except:
        raise
    
    return create_json_response(response_status, query_dict=None, body_key="partners", body_dict=partner_list)


@partner_resource.route("/v1/partners/<string:partner_id>", methods=["GET"])
def get_partner(partner_id):
    response_status = 200
    try:
        partner = PartnerController().get(partner_id)
    except:
        raise
    
    return create_json_response(response_status, query_dict=None, body_key="partner", body_dict=partner)


@partner_resource.route("/v1/partners", methods=["POST"])
def create_partner():
    response_status = 200
    params = request.get_json

    partner_dict = None
    try:
        partner = Partner(params["partner_id"], params["partner_name"], params=["partner_status"])
        partner_dict = PartnerController().create(parnter)
    except:
        raise

    return create_json_response(response_status, query_dict=None, body_key="partner", body_dict=partner_dict)


@partner_resource.route("/v1/partners/<string:partner_id>", methods=["PUT"])
def update_partner(partner_id):
    response_status = 200
    params = request.get_json

    partner_dict = None
    try:
        partner = Partner(params["partner_id"], params["partner_name"], params=["partner_status"])
        partner_dict = PartnerController().update(parnter)
    except:
        raise

    return create_json_response(response_status, query_dict=None, body_key="partner", body_dict=partner_dict)


@partner_resource.route("/v1/partners/<string:partner_id>", methods=["DELETE"])
def delete_partner(partner_id):
    response_status = 200

    try:
        res = PartnerController().delete(partner_id)
    except:
        raise

    return create_json_response(response_status, query_dict=None, body_key=None, body_dict=None)
