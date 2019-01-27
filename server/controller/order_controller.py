"""
"""

from server.utils import *
from server.models.order import Order
from server.models.order_product import OrderProduct
from server.models.order_payment import OrderPayment
#from server.models.order_payment_log import OrderPaymentLog
from server.data.cart_data import CartData
from server.data.order_data import OrderData


class OrderController(object):
    _orderData = OrderData()

    def __init__(self):
        pass

    def get_list_by_user_id(self, user_id=None, q=None, offset=0, fetch=20):
        order_list = None
        try:
            order_list = self._orderData.get_list_by_user_id(user_id, q, offset, fetch)
        except:
            raise
        
        return order_list


    def get(self, order_id):
        order_dict = None
        try:
            order_dict = self._orderData.get(order_id)
            order_dict["order_products"] = self._orderData.get_products(order_id)
            order_dict["order_payments"] = self._orderData.get_payments(order_id)
        except:
            raise

        return order_dict


    def create(self, user_id, platform_type=None, app_type=None):
        order_dict = None
        try:
            order_id = self._orderData.create(user_id, platform_type, app_type)
            order_dict = self._orderData.get(order_id)
            CartData().clear(user_id)

        except:
            raise

        return order_dict


    def cancel(self, order_id):
        try:
            self._orderData.cancel(order_id)
        except:
            raise


    def get_products(self, order_id):
        try:
            self._orderData.get_products(order_id)
        except:
            raise

    
    def get_payments(self, order_id):
        try:
            self._orderData.get_payments(order_id)
        except:
            raise


    def create_payment(self, order_id, method_code, payment_currency, payment_amount):
        """
        Create payment for a order and change status to 'completed'
        """
        try:
            payment_no = self._orderData.create_payment(order_id, method_code, payment_currency, payment_amount)
            self._orderData.change_status(order_id, 200)

        except:
            raise
