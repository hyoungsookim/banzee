"""
"""

from server.utils import *
from server.models.payment_method import PaymentMethod
from server.data import base
from server.data.helper import ConnectionHelper
from server.app import db


class PaymentMethodData(base.Data):
    """
    Payment method data class for accssing database
    """

    def __init__(self):
        pass


    def get_list(self):
        _rows = db.session.query(PaymentMethod).all()
        rows = [row.to_dict() for row in _rows]

        return rows


    def get(self, method_code):
        row = db.session.query(PaymentMethod).\
                filter(PaymentMethod.method_code == method_code).one_or_none()
        return row.to_dict()


    def create(self, paymentMethod):
        if not isinstance(paymentMethod, PaymentMethod):
            raise TypeError("Should be an instance of PaymentMethod class")

        try:
            db.session.add(paymentMethod)
            db.session.commit()
        except:
            db.session.rollback()
            return None

        return paymentMethod


    def update(self, paymentMethod):
        if not isinstance(paymentMethod, PaymentMethod):
            raise TypeError("Should be an instance of PaymentMethod class")

        try:
            db.session.query(PaymentMethod).\
                filter(PaymentMethod.method_code == paymentMethod.method_code).\
                update({
                    "method_status": paymentMethod.method_status,
                    "method_name": paymentMethod.method_name,
                    "method_type": paymentMethod.method_type,
                    "updated_at": get_current_datetime_str()
                })
            db.session.commit()
        except:
            db.session.rollback()
            return None

        return paymentMethod


    def delete(self, method_code):
        try:
            db.session.query(PaymentMethod).\
                filter(PaymentMethod.method_code == method_code).\
                delete()
            db.session.commit()
        except:
            db.session.rollback()
            return False
        
        return True
