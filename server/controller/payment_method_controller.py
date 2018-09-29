"""
"""

from server.utils import *
from server.models.payment_method import PaymentMethod
from server.models.payment_method_property import PaymentMethodProperty
from server.data.payment_method_data import PaymentMethodData
from server.data.payment_method_property_data import PaymentMethodPropertyData


class PaymentMethodController(object):
    methodData = PaymentMethodData()
    methodPropertyData = PaymentMethodPropertyData()

    def __init__(self):
        pass

    def get_list(self, q, offset=0, fetch=20):
        return self.methodData.get_list(q, offset, fetch)

    def get(self, method_code):
        return self.methodData.get(method_code)

    def create(self, paymentMethod):
        return self.methodData.create(paymentMethod)

    def update(self, paymentMethod):
        return self.methodData.update(paymentMethod)

    def delete(self, method_code):
        return self.methodData.delete(method_code)

    def get_property_list(self, method_code):
        return self.methodPropertyData.get_list(method_code)
    
    def get_property(self, method_code, property_type):
        return self.methodPropertyData.get(method_code, property_type)
        
    def set_property(self, method_code, property_type, property_value=None):
        return self.methodPropertyData.set(
            method_code, property_type, property_value)
    
    def delete_property(self, method_code, property_type):
        return self.methodPropertyData.delete(method_code, property_type)
