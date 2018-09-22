"""
"""

from server.utils import *
from server.models.payment_method import PaymentMethod
from server.data.payment_method_data import PaymentMethodData


class PaymentMethodController(object):

    def __init__(self):
        pass

    def get_list(self, q, offset=0, fetch=20):
        pass

    def get(self, method_code):
        pass

    def create(self, paymentMethod):
        pass

    def update(self, paymentMethod):
        pass

    def delete(self, method_code):
        pass
