"""
"""

import simplejson as json

from server.utils import *
from server.models.partner import Partner
from server.data.partner_data import PartnerData


class PartnerController(object):
    partnerData = PartnerData()

    def __init__(self):
        pass

    def get_list(self, q, offset=0, fetch=20):
        return self.partnerData.get_list(None, offset, fetch)
    
    def get(self, partner_id):
        return json.dumps(self.partnerData.get(partner_id), 
                sort_keys=False, encoding="utf-8", use_decimal=True, indent=4, default=str)

    def create(self, partner):
        return self.partnerData.create(partner)

    def update(self, partner):
        return self.partnerData.update(partner)

    def delete(self, partner_id):
        return self.partnerData.delete(partner_id)
