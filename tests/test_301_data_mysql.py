import pytest
# import uuid
# import decimal

from server.models.partner import Partner
from server.data.partner_data import PartnerData


class TestPartnerData(object):
    info = Partner(partner_id='XXX', partner_name='TEST_PARTNER', partner_status=200)

    data = PartnerData()

    def test_get_list(self):
        assert self.data.get_list() is not None

    def test_create_200_success(self):
        assert self.data.create(self.info) == True
