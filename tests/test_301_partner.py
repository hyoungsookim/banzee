import pytest
# import uuid
# import decimal

from server.models.partner import Partner
from server.controller.partner_controller import PartnerController


class TestPartnerData(object):
    info = Partner(partner_id='XXX', partner_name='TEST_PARTNER', partner_status=200)

    controller = PartnerController()

    def test_get_list(self):
        assert self.controller.get_list(None, 0, 20) is not None

    def test_get(self):
        assert self.controller.get("VINCLE") is not None

    def test_create_200_success(self):
        assert self.controller.create(self.info) == True

    def test_update_200_success(self):
        self.info.partner_status = 0
        self.info.partner_name = "UNIT_TEST"
        assert self.controller.update(self.info) == True

    def test_delete_200_success(self):
        assert self.controller.delete('XXX') == True

