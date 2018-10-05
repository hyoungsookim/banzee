"""
"""

from server.utils import *
from server.models.partner import Partner
from server.data.partner_data import PartnerData
from server.exceptions import *


class PartnerController(object):
    _partnerData = PartnerData()

    def __init__(self):
        pass


    def get_list(self, q, offset=0, fetch=20):
        partner_list = None
        try:
            partner_list = self._partnerData.get_list(q, offset, fetch)
        except:
            raise

        return partner_list

    
    def get(self, partner_id):
        partner_dict = None
        try:
            partner_dict = self._partnerData.get(partner_id)
        except:
            raise

        return partner_dict


    def create(self, partner):
        partner_dict = None
        try:
            partner_dict = self._partnerData.create(partner)
        except:
            raise

        return partner_dict


    def update(self, partner):
        partner_dict = None
        try:
            partner_dict = self._partnerData.update(partner)
        except:
            raise

        return partner_dict 

    def delete(self, partner_id):
        return self._partnerData.delete(partner_id)
