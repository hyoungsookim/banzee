"""
"""

from server.utils import *
from server.models.partner import Partner
from server.data.partner_data import PartnerData


class PartnerController(object):

    def __init__(self):
        pass

    def get_list(self, q, offset=0, fetch=20):
        pass
    
    def get(self, partner_id):
        pass

    def create(self, partner):
        pass

    def update(self, partner):
        pass

    def delete(self, partner_id):
        pass
