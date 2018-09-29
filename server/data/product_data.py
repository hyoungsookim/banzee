"""
"""

from datetime import datetime

from server.utils import *
from server.models.product import Product
from server.data import base
from server.data.helper import ConnectionHelper
from server.app import db


class ProductData(base.Data):
    """
    Partner data class for accssing database
    """
    def __init__(self):
        pass


    def get_list(self, q=None, offset=1, fetch=20):
        _rows = db.session.query(Product).all()
        rows = [row.to_dict() for row in _rows]
        return rows


    def get(self, product_id):
        row = db.session.query(Product).\
                filter(Product.product_id == product_id).one_or_none()
        return row.to_dict()


    def create(self, product):
        if not isinstance(product, Product):
            raise TypeError("product should be an instance of Product class")

        try:
            db.session.add(product)
            db.session.commit()
        except:
            db.session.rollback()
            return None

        return product


    def update(self, product):
        if not isinstance(product, Product):
            raise TypeError("product should be an instance of Product class")
        
        try:
            db.session.query(Product).\
                filter(Product.product_id == product.product_id).\
                update({
                    "product_status": product.product_status,
                    "product_name": product.product_name,
                    "product_type": product.product_type,
                    "updated_at": get_current_datetime_str(),
                    "product_description": product.product_description
                })
            db.session.commit()
        except:
            db.session.rollback()
            return None

        return product


    def delete(self, product_id):
        try:
            db.session.query(Product).\
                filter(Product.product_id == product_id).\
                delete()
            db.session.commit()
        except:
            db.session.rollback()
            return False
        
        return True
