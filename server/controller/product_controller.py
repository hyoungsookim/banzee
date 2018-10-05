"""
"""

from server.utils import *
from server.models.product import Product
from server.data.product_data import ProductData


class ProductController(object):
    _productData = ProductData()

    def __init__(self):
        pass

    def get_list(self, q=None, offset=0, fetch=20):
        product_list = None
        try:
            product_list = self._productData.get_list(q, offset, fetch)
        except:
            raise

        return product_list


    def get(self, product_id):
        product_dict = None
        try:
            product_dict = self._productData.get(product_id)
        except:
            raise

        return product_dict


    def create(self, product):
        product_dict = None
        try:
            product_dict = self._productData.create(product)
        except:
            raise

        return product_dict


    def update(self, product):
        product_dict = None
        try:
            return self._productData.update(product)
        except:
            raise
        
        return product_dict

        
    def delete(self, product_id):
        return self._productData.delete(product_id)
