from flask import Blueprint, request

from server.config import Config
from server.api.response_resource import *


system_resource = Blueprint("system_resource", "system_resource")

@system_resource.route("/", methods=['GET'])
def check_health():
    """
    Health check
    """
    #return application.static_folder
    return system_resource.send_static_file('health.html')


@system_resource.route("/v1/system", methods=['GET'])
def check_system():
    """
    Ping to API server
    """

    level = int(request.args.get("level", 0))

    res_dict = dict()
    if level >= 1:
        res_dict.update(DATABASE_HOST=Config.DATABASE_HOST)

    return create_json_response(response_status=200, query_dict=None, body_key="system", body_dict=res_dict)


