"""
"""

from server.utils import *
from server.models.cart import Cart
from server.data.cart_data import CartData
from server.controller.user_controller import UserController
from server.exceptions import *


class CartController(object):
    _cartData = CartData()

    def __init__(self):
        pass


    def get_list(self, user_id):
        product_list = None
        try:
            product_list = self._cartData.get_list(user_id)
        except:
            raise

        return product_list

    
    def add(self, user_id, product_id):
        product_dict = None
        try:
            self._cartData.add(user_id, product_id)
            product_dict = self.get_list(user_id)
            
        except:
            raise

        return product_dict


    def update_quantity(self, user_id, product_id, product_quantity=1):
        product_dict = None
        try:
            self._cartData.update_quantity(user_id, product_id, product_quantity)
            product_dict = self.get_list(user_id)
        except:
            raise

        return product_dict 


    def delete(self, user_id, product_id):
        product_dict = None
        try:
            self._cartData.delete(user_id, product_id)
            product_dict = self.get_list(user_id)
        except:
            raise

        return product_dict 


    def clear(self, order_id):
        try:
            self._cartData.delete(order_id)
        except:
            raise
