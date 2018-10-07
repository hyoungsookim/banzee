import urllib.request
import json
import pytest
# import uuid
# import decimal

from server.models.payment_method import PaymentMethod
#from server.controller.payment_method_controller import PaymentMethodController


base_url = "http://localhost:5000/v1/payment_methods"
headers = {'Content-Type': 'application/json;charset=UTF-8'}

class TestPaymentMethod(object):
    #info = PaymentMethod(
    #        method_code='XXX', 
    #        method_status=200, 
    #        method_name='TEST', 
    #        method_type='CC')

    #controller = PaymentMethodController()

    def test_get_list_200(self):
        res = urllib.request.urlopen(base_url)
        data = str(res.read())

        #assert self.controller.get_list(q=None, offset=1, fetch=20) is not None
        assert "200" in data
        assert "payment_methods" in data


    def test_get_200(self):
        res = urllib.request.urlopen(base_url + '/STRIPECARD')
        data = str(res.read())

        #assert self.controller.get("STRIPECARD") is not None
        assert "200" in data
        assert "payment_method" in data


    def test_create_200(self):
        data = '{ \
                    "method_code": "XXX", \
                    "method_name": "test payment method", \
                    "method_status": 200, \
                    "method_type": "CC" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url,
                                     data=data,
                                     headers=headers,
                                     method='POST')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        #assert self.controller.create(self.info) is not None
        assert "200" in data
        assert "payment_method" in data


    def test_update_200(self):
        data = '{ \
                    "method_name": "Test Payment method", \
                    "method_status": 0, \
                    "method_type": "CR" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url + '/STRIPECARD', 
                                    data=data,
                                    headers=headers,
                                    method='PUT')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data
        assert "method_code" in data


    def test_delete_200(self):
        req = urllib.request.Request(base_url + '/STRIPECARD',
                                    headers=headers,
                                    method='DELETE')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data


    #def test_set_property_200(self):
    #    assert self.controller.set_property(self.info.method_code, 100, "TEST_VALUE") == True

    #def test_get_property_list_200(self):
    #    assert self.controller.get_property_list(self.info.method_code) is not None

    #def test_get_property_200(self):
    #    assert self.controller.get_property(self.info.method_code, 100) is not None

    #def test_delete_property_200(self):
    #    assert self.controller.delete_property(self.info.method_code, 100)
