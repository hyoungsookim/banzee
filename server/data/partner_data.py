"""
"""

from datetime import datetime

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


    def get_list(self):
        rows = Partner.query.all()
        return rows


    def get(self, partner_id):
        row = Partner.query.filter_by(partner_id=partner_id)
        return row


    def create(self, partner):
        if not isinstance(partner, Partner):
            raise TypeError("Should be an instance of Partner class")

        try:
            db.session.add(partner)
            db.session.commit()
        except:
            db.session.rollback()
            
        return True


    def update(self, partner):
        if not isinstance(partner, Partner):
            raise TypeError("Should be an instance of Partner class")

        try:
            db.session.query(Partner).filter_by(partner_id=partner.partner_id).\
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


    def delete(self, partner):
        if not isinstance(partner, Partner):
            raise TypeError("Should be an instance of Partner class")

        try:
            db.session.delete(partner)
            db.session.commit()
        except:
            db.session.rollback()
            return False
        
        return True
