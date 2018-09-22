"""
"""

from server.utils import *
from server.models.orders import Order
from server.models.order_product import OrderProduct
from server.models.order_payment import OrderPayment
from server.models.order_payment_log import OrderPaymentLog
from server.data.order_data import OrderData


class OrderController(object):

    def __init__(self):
        pass

    def get_list(self, q, offset=0, fetch=20):
        pass

    def get_list_by_user_id(self, user_id, offset=0, fetch=20):
        pass
        
    def get(self, order_id):
        pass

    def create(self, order):
        pass

    def update(self):
        pass

    def cancel(self, order_id):
        pass

    def change_status(self, order_id, new_status):
        pass
