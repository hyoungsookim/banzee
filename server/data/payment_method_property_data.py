"""
"""

from server.utils import *
from server.models.payment_method_property import PaymentMethodProperty
from server.data import base
from server.data.helper import ConnectionHelper
from server.app import db


class PaymentMethodProperty(object):
    """
    Payment method property data class for accssing database
    """

    def __init__(self):
        pass


    def get_list(self, method_code):
        rows = db.session.query(PaymentMethodProperty).\
                filter(PaymentMethod.method_code == method_code).all()
        return rows

    
    def get(self, method_code, property_type):
        row = db.session.query(PaymentMethodProperty).\
                filter(PaymentMethodProperty.method_code == method_code).\
                filter(PaymentMethodProperty.property_type == property_type).\
                one_or_none()
        return row


    def set(self, paymentMethodProperty):
        if not isinstance(paymentMethodProperty, PaymentMethodProperty):
            raise TypeError("Should be an instance of PaymentMethodProperty class")

        try:
            db.session.add(paymentMethodProperty)
            db.session.commit()
        except:
            db.session.rollback()
            
        return True
    

    def delete(self, method_code, property_type):
        try:
            row = db.session.query(PaymentMethodProperty).\
                filter(PaymentMethodProperty.method_code == method_code).\
                filter(PaymentMethodProperty.property_type == property_type).\
                delete()
            db.session.commit()
        except:
            db.session.rollback()
            return False
        
        return True