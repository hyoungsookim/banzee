import pytest
# import uuid
# import decimal

from server.models.product import Product
from server.data.product_data import ProductData


class TestProduct(object):
    info = Product(product_id="PRODUCT_ID_TEST", 
                   product_status=200,
                   product_name="PRODUCT_NAME_TEST",
                   product_type="SERVICE",
                   product_description=None)

    data = ProductData()

    def test_create_200_success(self):
        assert self.data.create(self.info) is not None

    def test_get_list(self):
        assert self.data.get_list() is not None

    def test_get(self):
        assert self.data.get("PRODUcT_ID_TEST") is not None

    def test_update_200_success(self):
        self.info.product_status = 0
        self.info.product_name = "TEST_PRODUCT_NAME"
        self.info.product_type = "ITEM"
        self.info.product_description = "PRODUCT_DESCRIPTION"
        assert self.data.update(self.info) is not None

    def test_delete_200_success(self):
        assert self.data.delete('PRODUCT_ID_TEST') == True
