"""
"""

import datetime


def is_none_or_empty(param, return_value):
    """
    Args:
        param :
        return_value :
    Returns:
    """
    return return_value if param is None or param == '' else param


def get_current_datetime_str():
    """
    Parameters:
    Returns:
    """
    return str(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f"))
