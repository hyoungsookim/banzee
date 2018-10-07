"""
"""

from flask import Blueprint, request

from server.controller.product_controller import ProductController
from server.models.product import Product
from server.exceptions import BanzeeException
from server.api.response_resource import *


product_resource = Blueprint("product_resource", "product_resource")

@product_resource.route("/v1/products", methods=["GET"])
def get_product_list():
    q = request.args.get("q", None)
    offset = request.args.get("offset", 0, type=int)
    fetch = request.args.get("fetch", 20, type=int)

    response_status = 200
    product_list = None
    try:
        product_list = ProductController().get_list(q, offset, fetch)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="products", body_dict=product_list)


@product_resource.route("/v1/products/<string:product_id>", methods=["GET"])
def get_product(product_id):
    response_status = 200
    product_dict = None
    try:
        product_dict = ProductController().get(product_id)

    except BanzeeException as ex:
        response_status = ex.code
    
    return create_json_response(response_status, query_dict=None, body_key="product", body_dict=product_dict)


@product_resource.route("/v1/products", methods=["POST"])
def create_product():
    response_status = 200
    params = request.get_json()

    product_dict = None
    try:
        product = Product(product_id=None, 
                          product_status = params["product_status"], 
                          product_name = params["product_name"], 
                          product_type = params["product_type"], 
                          product_description = params["product_description"])
        product_dict = ProductController().create(product)

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key="product", body_dict=product_dict)


@product_resource.route("/v1/products/<string:product_id>", methods=["PUT"])
def update_product(product_id):
    response_status = 200
    params = request.get_json()

    product_dict = None
    try:
        product = Product(product_id, 
                          params["product_status"], 
                          params["product_name"], 
                          params["product_type"], 
                          params["product_description"])
        product_dict = ProductController().update(product)

    except KeyError as ex:
        response_status = 400

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key="product", body_dict=product_dict)


@product_resource.route("/v1/products/<string:product_id>", methods=["DELETE"])
def delete_product(product_id):
    response_status = 200

    try:
        res = ProductController().delete(product_id)

    except BanzeeException as ex:
        response_status = ex.code

    return create_json_response(response_status, query_dict=None, body_key=None, body_dict=None)
