"""
"""

from server.utils import *
from server.models.product import Product
from server.data.product_data import ProductData


class ProductController(object):

    def __init__(self):
        pass

    def get_list(self, q, offset=0, fetch=20):
        pass

    def get(self, product_id):
        pass

    def create(self, product):
        pass

    def update(self, product):
        pass

    def delete(self, product_id):
        pass
