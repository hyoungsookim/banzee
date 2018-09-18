import pytest
# import uuid
# import decimal

from server.models.partner import Partner
from server.models.payment_method import PaymentMethod
from server.models.transaction_type import TransactionType
from server.data.partner_data import PartnerData
from server.data.payment_method_data import PaymentMethodData
from server.data.transaction_type_data import TransactionTypeData


class TestPartnerData(object):
    info = Partner(partner_id='XXX', partner_name='TEST_PARTNER', partner_status=200)

    data = PartnerData()

    def test_get_list(self):
        assert self.data.get_list() is not None

    def test_get(self):
        assert self.data.get("VINCLE") is not None

    def test_create_200_success(self):
        assert self.data.create(self.info) == True

    def test_update_200_success(self):
        self.info.partner_status = 0
        self.info.partner_name = "UNIT_TEST"
        assert self.data.update(self.info) == True

    def test_delete_200_success(self):
        assert self.data.delete(self.info) == True


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
        assert self.data.delete(self.info) == True


class TestTransactionType(object):
    info = TransactionType(trx_type=999, trx_type_name="TEST_TYPE", trx_type_description="description")

    data = TransactionTypeData()

    def test_create_200_success(self):
        assert self.data.create(self.info) == True

    def test_get_list(self):
        assert self.data.get_list() is not None

    def test_get(self):
        assert self.data.get(999) is not None

    def test_update_200_success(self):
        self.info.trx_type_name = "TYPE_TEST"
        self.info.trx_type_description = "UNIT_TEST"
        assert self.data.update(self.info) == True

    def test_delete_200_success(self):
        assert self.data.delete(self.info) == True
