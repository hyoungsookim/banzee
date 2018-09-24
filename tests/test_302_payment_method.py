import pytest
# import uuid
# import decimal

from server.models.payment_method import PaymentMethod
from server.data.payment_method_data import PaymentMethodData


class TestPaymentMethod(object):
    info = PaymentMethod(method_code='XXX', method_status=200, method_name='TEST', method_type='CC')

    data = PaymentMethodData()

    def test_get_list(self):
        assert self.data.get_list() is not None

    def test_get(self):
        assert self.data.get("STRIPECARD") is not None

    def test_create_200_success(self):
        assert self.data.create(self.info) == True

    def test_update_200_success(self):
        self.info.method_status = 0
        self.info.method_name = "UNIT_TEST"
        self.info.method_type = "CP"
        assert self.data.update(self.info) == True

    def test_delete_200_success(self):
        assert self.data.delete('XXX') == True
