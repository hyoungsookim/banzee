"""
"""

from server.utils import *
from server.models.product import Product
from server.data.product_data import ProductData


class ProductController(object):
    data = ProductData()

    def __init__(self):
        pass

    def get_list(self, q=None, offset=0, fetch=20):
        return self.data.get_list(q, offset, fetch)

    def get(self, product_id):
        return self.data.get(product_id)

    def create(self, product):
        return self.data.create(product)

    def update(self, product):
        return self.data.update(product)

    def delete(self, product_id):
        return self.data.delete(product_id)
