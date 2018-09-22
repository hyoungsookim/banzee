"""
"""

from server.utils import *
from server.models.payment_method import PaymentMethod
from server.data.payment_method_data import PaymentMethodData


class TransactionController(object):

    def __init__(self):
        pass

    def get_list(self, q, offset=0, fetch=20):
        pass

    def get(self, trx_id):
        pass

    def create(self, transaction):
        pass

    def update(self, transaction):
        pass

    def delete(self, trx_id):
        pass
