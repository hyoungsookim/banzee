import pytest
# import uuid
# import decimal

from server.models.orders import Order
from server.models.partner import Partner
from server.models.payment_method import PaymentMethod
from server.models.product import Product
from server.models.transaction_type import TransactionType
from server.models.user import User
from server.data.order_data import OrderData
from server.data.partner_data import PartnerData
from server.data.payment_method_data import PaymentMethodData
from server.data.product_data import ProductData
from server.data.transaction_type_data import TransactionTypeData
from server.data.user_data import UserData


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
        assert self.data.delete('XXX') == True


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
        assert self.data.delete('TYPE_TEST') == True


class TestUser(object):
    info = User(user_id="USER_ID_TEST", 
                partner_id="VINCLE",
                user_status=200,
                user_type=1,
                user_level=100,
                first_name="TEST_FIRST_NAME",
                last_name="TEST_LAST_NAME")

    data = UserData()

    def test_get_list(self):
        assert self.data.get_list() is not None

    def test_get(self):
        assert self.data.get("TEST_USER_ID") is not None

    def test_create_200_success(self):
        assert self.data.create(self.info) == True

    def test_update_200_success(self):
        self.info.user_status = 0
        self.info.user_type = 2
        self.info.user_level = 101
        self.info.first_name = "FIRST_NAME_TEST"
        self.info.last_name = "LAST_NAME_TEST"
        assert self.data.update(self.info) == True

    def test_delete_200_success(self):
        assert self.data.delete('USER_ID_TEST') == True


class TestProduct(object):
    info = Product(product_id="PRODUCT_ID_TEST", 
                   product_status=200,
                   product_name="PRODUCT_NAME_TEST",
                   product_type="SERVICE",
                   product_description=None)

    data = ProductData()

    def test_create_200_success(self):
        assert self.data.create(self.info) == True

    def test_get_list(self):
        assert self.data.get_list() is not None

    def test_get(self):
        assert self.data.get("PRODUcT_ID_TEST") is not None

    def test_update_200_success(self):
        self.info.product_status = 0
        self.info.product_name = "TEST_PRODUCT_NAME"
        self.info.product_type = "ITEM"
        self.info.product_description = "PRODUCT_DESCRIPTION"
        assert self.data.update(self.info) == True

    def test_delete_200_success(self):
        assert self.data.delete('PRODUCT_ID_TEST') == True


class TestOrder(object):
    info = Order(order_id="ORDER_ID_TEST",
                 user_no=2, 
                 order_status=200,
                 order_amount=123,
                 tax_amount=10,
                 total_amount=133,
                 platform_type=None,
                 app_type=None)

    data = OrderData()

    def test_create_200_success(self):
        assert self.data.create(self.info) == True

    def test_get_list(self):
        assert self.data.get_list() is not None

    def test_get(self):
        assert self.data.get("ORDER_ID_TEST") is not None

    def test_update_200_success(self):
        self.info.order_status = 0
        self.info.order_amount = 100
        self.info.tax_amount = 8.5
        self.info.total_amount = 108.5
        self.info.platform_type = "APPLE"
        self.info.app_type = "IPHONE"
        assert self.data.update(self.info) == True

    def test_delete_200_success(self):
        assert self.data.delete('ORDER_ID_TEST') == True
