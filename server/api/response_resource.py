"""
"""

import datetime
import simplejson as json
from flask import make_response, Response

from server.messages import *


class ResponseInfo(object):
    """
    """
    def __init__(self, code, message):
        self.__response_code = code
        self.__response_message = get_message(code)
        self.__response_datetime = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


    def to_dict(self):
        result = dict()
        result.update(response_code=self.response_code, 
                      response_message=self.response_message, 
                      response_datetime=self.response_datetime)

        return result

    @property
    def response_code(self):
        return self.__response_code

    @property
    def response_message(self):
        return self.__response_message

    @property
    def response_datetime(self):
        return self.__response_datetime


def convert_dict_to_response(response_dict):
    """
    Convert Dict to Flask Response object
    """
    # status = int(response_dict['response']['response_code'])
    response_str = json.dumps(response_dict,
                              sort_keys=False,
                              encoding="utf-8",
                              use_decimal=True,
                              indent=4,
                              default=str)
    response = make_response(response_str, 200)
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'

    return response


def get_response_info(status=200, attribute=None):
    """
    """
    return ResponseInfo(status, "message").to_dict()


def create_json_response(response_status, 
                         query_dict=None, 
                         body_key=None, 
                         body_dict=None):
    res_dict = dict()
    res_dict["response"] = get_response_info(response_status)
    if query_dict:
        res_dict.update(offset=query_dict["offset"], fetch=query_dict["fetch"])
    res_dict[body_key] = body_dict

    return convert_dict_to_response(res_dict)
