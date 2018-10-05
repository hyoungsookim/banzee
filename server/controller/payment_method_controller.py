"""
"""

from server.utils import *
from server.models.payment_method import PaymentMethod
from server.models.payment_method_property import PaymentMethodProperty
from server.data.payment_method_data import PaymentMethodData
from server.data.payment_method_property_data import PaymentMethodPropertyData


class PaymentMethodController(object):
    _methodData = PaymentMethodData()
    _methodPropertyData = PaymentMethodPropertyData()

    def __init__(self):
        pass

    def get_list(self, q, offset=0, fetch=20):
        method_list = None
        try:
            method_list = self._methodData.get_list(q, offset, fetch)
        except:
            raise

        return method_list


    def get(self, method_code):
        method_dict = None
        try:
            method_dict = self._methodData.get(method_code)
        except:
            raise
        
        return method_dict


    def create(self, paymentMethod):
        method_dict = None
        try:
            method_dict = self._methodData.create(paymentMethod)
        except:
            raise

        return method_dict


    def update(self, paymentMethod):
        method_dict = None
        try:
            method_dict = self._methodData.update(paymentMethod)
        except:
            raise

        return method_dict


    def delete(self, method_code):
        return self._methodData.delete(method_code)


    def get_property_list(self, method_code):
        return self._methodPropertyData.get_list(method_code)
    
    def get_property(self, method_code, property_type):
        return self._methodPropertyData.get(method_code, property_type)
        
    def set_property(self, method_code, property_type, property_value=None):
        return self._methodPropertyData.set(
            method_code, property_type, property_value)
    
    def delete_property(self, method_code, property_type):
        return self._methodPropertyData.delete(method_code, property_type)
