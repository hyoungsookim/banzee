import pytest
# import uuid
# import decimal

from server.models.payment_method import PaymentMethod
from server.controller.payment_method_controller import PaymentMethodController


class TestPaymentMethod(object):
    info = PaymentMethod(
            method_code='XXX', 
            method_status=200, 
            method_name='TEST', 
            method_type='CC')

    controller = PaymentMethodController()

    def test_get_list(self):
        assert self.controller.get_list(q=None, offset=1, fetch=20) is not None

    def test_get(self):
        assert self.controller.get("STRIPECARD") is not None

    def test_create_200_success(self):
        assert self.controller.create(self.info) is not None

    def test_update_200_success(self):
        self.info.method_status = 0
        self.info.method_name = "UNIT_TEST"
        self.info.method_type = "CP"
        assert self.controller.update(self.info) is not None

    def test_delete_200_success(self):
        assert self.controller.delete('XXX') == True


    def test_set_property_200_success(self):
        assert self.controller.set_property(self.info.method_code, 100, "TEST_VALUE") == True

    def test_get_property_list(self):
        assert self.controller.get_property_list(self.info.method_code) is not None

    def test_get_property(self):
        assert self.controller.get_property(self.info.method_code, 100) is not None

    def test_delete_property_200_succss(self):
        assert self.controller.delete_property(self.info.method_code, 100)
