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
    Product data class for accssing database
    """
    def __init__(self):
        pass


    def get_list(self):
        rows = Order.query.all()
        return rows


    def get(self, order_id):
        row = Order.query.filter_by(order_id=order_id)
        return row


    def create(self, order):
        if not isinstance(order, Order):
            raise TypeError("Should be an instance of Order class")

        try:
            db.session.add(order)
            db.session.commit()
        except:
            db.session.rollback()
            
        return True


    def update(self, order):
        if not isinstance(order, Order):
            raise TypeError("Should be an instance of Order class")

        try:
            db.session.query(Order).filter_by(order_id=order.order_id).\
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
            return False

        return True


    def delete(self, order):
        if not isinstance(order, Order):
            raise TypeError("Should be an instance of Order class")

        try:
            db.session.delete(order)
            db.session.commit()
        except:
            db.session.rollback()
            return False
        
        return True
