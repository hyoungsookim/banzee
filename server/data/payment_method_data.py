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
        rows = PaymentMethod.query.all()
        return rows


    def get(self, method_code):
        row = PaymentMethod.query.filter_by(method_code=method_code)
        return row


    def create(self, paymentMethod):
        try:
            db.session.add(paymentMethod)
            db.session.commit()
        except:
            db.session.rollback()
            
        return True


    def update(self, paymentMethod):
        try:
            db.session.query(PaymentMethod).filter_by(method_code=paymentMethod.method_code).\
                update({
                            "method_status": paymentMethod.method_status,
                            "method_name": paymentMethod.method_name,
                            "method_type": paymentMethod.method_type,
                            "updated_at": get_current_datetime_str()
                        })
            db.session.commit()
        except:
            db.session.rollback()
            return False

        return True


    def delete(self, paymentMethod):
        try:
            db.session.delete(paymentMethod)
            db.session.commit()
        except:
            db.session.rollback()
            return False
        
        return True
