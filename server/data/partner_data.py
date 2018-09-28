"""
"""

from server.utils import *
from server.models.partner import Partner
from server.data import base
from server.data.helper import ConnectionHelper
from server.app import db


class PartnerData(base.Data):
    """
    Partner data class for accssing database
    """
    def __init__(self):
        pass


    def get_list(self, q=None, offset=0, fetch=20):
        rows = db.session.query(Partner).all()
        return rows


    def get(self, partner_id):
        row = db.session.query(Partner).\
                filter(Partner.partner_id == partner_id).one_or_none()
        return row


    def create(self, partner):
        if not isinstance(partner, Partner):
            raise TypeError("'partner' parameter should be an instance of Partner class")

        try:
            db.session.add(partner)
            db.session.commit()
        except:
            db.session.rollback()
            
        return True


    def update(self, partner):
        if not isinstance(partner, Partner):
            raise TypeError("'partner' parameter should be an instance of Partner class")

        try:
            db.session.query(Partner).\
                filter(Partner.partner_id == partner.partner_id).\
                update({
                    "partner_status": partner.partner_status,
                    "partner_name": partner.partner_name,
                    "updated_at": get_current_datetime_str()
                })
            db.session.commit()
        except:
            db.session.rollback()
            return False

        return True


    def delete(self, partner_id):
        try:
            db.session.query(Partner).\
                filter(Partner.partner_id == partner_id).\
                delete(synchronize_session=False)
            db.session.commit()
        except:
            db.session.rollback()
            return False
        
        return True
