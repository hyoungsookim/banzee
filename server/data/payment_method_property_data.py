"""
"""

from server.utils import *
from server.models.payment_method_property import PaymentMethodProperty
from server.data import base
from server.data.helper import ConnectionHelper
from server.db_factory import db


class PaymentMethodPropertyData(object):
    """
    Payment method property data class for accssing database
    """

    def __init__(self):
        pass


    def get_list(self, method_code):
        _rows = db.session.query(PaymentMethodProperty).\
                filter(PaymentMethodProperty.method_code == method_code).all()
        rows = [row.to_dict() for row in _rows]

        return rows

    
    def get(self, method_code, property_type):
        row = db.session.query(PaymentMethodProperty).\
                filter(PaymentMethodProperty.method_code == method_code).\
                filter(PaymentMethodProperty.property_type == property_type).\
                one_or_none()
        return row.to_dict()


    def set(self, method_code, property_type, property_value=None):
        property = PaymentMethodProperty(
                        method_code, 
                        property_type, 
                        property_value)

        try:
            db.session.add(property)
            db.session.commit()
        except:
            db.session.rollback()
            return False

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
