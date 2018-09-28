"""
"""

from datetime import datetime

from server.utils import *
from server.models.orders import Order
from server.data import base
from server.data.helper import ConnectionHelper
from server.app import db


class OrderData(base.Data):
    """
    Order data class for accssing database
    """
    def __init__(self):
        pass


    def get_list(self):
        _rows = db.session.query(Order).all()
        rows = [row.to_dict() for row in _rows]
        return rows


    def get(self, order_id):
        row = db.session.query(Order).\
                filter(Order.order_id == order_id).one_or_none()
        return row.to_dict()


    def create(self, order):
        if not isinstance(order, Order):
            raise TypeError("Should be an instance of Order class")

        try:
            db.session.add(order)
            db.session.commit()
        except:
            db.session.rollback()
            return None

        return order


    def update(self, order):
        if not isinstance(order, Order):
            raise TypeError("Should be an instance of Order class")

        try:
            db.session.query(Order).\
                filter(Order.order_id == order.order_id).\
                update({
                    "order_status": order.order_status,
                    "updated_at": get_current_datetime_str(),
                    "order_amount": order.order_amount,
                    "tax_amount": order.tax_amount,
                    "total_amount": order.total_amount,
                    "platform_type": order.platform_type,
                    "app_type": order.app_type
                })
            db.session.commit()
        except:
            db.session.rollback()
            return None

        return order


    def delete(self, order_id):
        try:
            db.session.query(Order).\
                filter(Order.order_id == order_id).\
                delete()
            db.session.commit()
        except:
            db.session.rollback()
            return False
        
        return True
