"""
"""

from sqlalchemy.exc import OperationalError

from server.utils import *
from server.models.partner import Partner
from server.data import DataBase
from server.data.helper import ConnectionHelper
from server.db_factory import db
from server.exceptions import *


class PartnerData(DataBase):
    """
    Partner data class for accssing database
    """
    def __init__(self):
        pass


    def get_list(self, q=None, offset=0, fetch=20):
        _rows = None
        try:
            _rows = db.session.query(Partner).all()

        except OperationalError as ex:
            raise InternalServerError(ex)

        rows = [row.to_dict() for row in _rows]

        return rows


    def get(self, partner_id):
        try:
            row = db.session.query(Partner).\
                    filter(Partner.partner_id == partner_id).one_or_none()

            if not row:
                raise ResourceNotFoundException

        except OperationalError as ex:
            raise InternalServerError(ex)
            
        return row.to_dict()


    def create(self, partner):
        if not isinstance(partner, Partner):
            raise TypeError("'partner' parameter should be an instance of Partner class")

        try:
            db.session.add(partner)
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raise

        return partner.to_dict()


    def update(self, partner):
        if not isinstance(partner, Partner):
            raise TypeError("'partner' parameter should be an instance of Partner class")

        try:
            partner.updated_at = get_current_datetime_str()
            #db.session.query(Partner).\
            #    filter(Partner.partner_id == partner.partner_id).\
            #    update({
            #        "partner_status": partner.partner_status,
            #        "partner_name": partner.partner_name,
            #        "updated_at": get_current_datetime_str()
            #    })
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raise

        return partner.to_dict()


    def delete(self, partner_id):
        try:
            db.session.query(Partner).\
                filter(Partner.partner_id == partner_id).\
                delete(synchronize_session=False)
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raise

        return True
