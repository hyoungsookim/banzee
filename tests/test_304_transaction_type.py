import pytest
# import uuid
# import decimal

from server.models.transaction_type import TransactionType
from server.controller.transaction_type_controller import TransactionTypeController


class TestTransactionType(object):
    info = TransactionType(trx_type=999, trx_type_name="TEST_TYPE", trx_type_description="description")

    controller = TransactionTypeController()

    def test_create_200_success(self):
        assert self.controller.create(self.info) is not None

    def test_get_list(self):
        assert self.controller.get_list() is not None

    def test_get(self):
        assert self.controller.get(999) is not None

    def test_update_200_success(self):
        self.info.trx_type_name = "TYPE_TEST"
        self.info.trx_type_description = "UNIT_TEST"
        assert self.controller.update(self.info) is not None

    def test_delete_200_success(self):
        assert self.controller.delete(self.info.trx_type) == True

