"""
"""


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

    def get(self, partner_id):
        row = Partner.query.fillter_by(partner_id=partner_id)
        return row

    def get_list(self):
        rows = Partner.query.all()
        return rows


    def create(self, partner):
        try:
            db.session.add(partner)
            db.session.commit()
        except:
            db.session.rollback()

        return True


    def update(self, partner):
        try:
            db.session.add(partner)
            db.session.commit()
        except:
            db.session.rollback()

        return True

    def delete(self, partner):
        try:
            db.session.delete(partner)
            db.session.commit()
        except:
            db.session.rollback()
        
        return True
