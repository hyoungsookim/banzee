import pytest
# import uuid
# import decimal

from server.models.orders import Order
from server.data.order_data import OrderData


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
