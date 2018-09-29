import pytest
# import uuid
# import decimal

from server.models.product import Product
from server.controller.product_controller import ProductController


class TestProduct(object):
    info = Product(product_id="PRODUCT_ID_TEST", 
                   product_status=200,
                   product_name="PRODUCT_NAME_TEST",
                   product_type="SERVICE",
                   product_description=None)

    controller = ProductController()

    def test_create_200_success(self):
        assert self.controller.create(self.info) is not None

    def test_get_list(self):
        assert self.controller.get_list() is not None

    def test_get(self):
        assert self.controller.get("PRODUcT_ID_TEST") is not None

    def test_update_200_success(self):
        self.info.product_status = 0
        self.info.product_name = "TEST_PRODUCT_NAME"
        self.info.product_type = "ITEM"
        self.info.product_description = "PRODUCT_DESCRIPTION"
        assert self.controller.update(self.info) is not None

    def test_delete_200_success(self):
        assert self.controller.delete('PRODUCT_ID_TEST') == True
