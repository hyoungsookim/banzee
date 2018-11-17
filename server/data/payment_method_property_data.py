"""
"""

from sqlalchemy.exc import OperationalError

from server.utils import *
from server.models.payment_method_property import PaymentMethodProperty
from server.data import DataBase
from server.data.helper import ConnectionHelper
from server.db_factory import db
from server.exceptions import *


class PaymentMethodPropertyData(DataBase):
    """
    Payment method property data class for accssing database
    """

    def __init__(self):
        pass


    def get_list(self, method_code):
        _rows = None
        try:
            _rows = db.session.query(PaymentMethodProperty).\
                    filter(PaymentMethodProperty.method_code == method_code).all()

        except OperationalError as ex:
            raise InternalServerError(ex)

        rows = [row.to_dict() for row in _rows]

        return rows

    
    def get(self, method_code, property_type):
        try:
            row = db.session.query(PaymentMethodProperty).\
                    filter(PaymentMethodProperty.method_code == method_code).\
                    filter(PaymentMethodProperty.property_type == property_type).\
                    one_or_none()

            if not row:
                raise ResourceNotFoundException

        except OperationalError as ex:
            raise InternalServerError(ex)

        return row.to_dict()


    def set(self, method_code, property_type, property_value=None):
        property = PaymentMethodProperty(
                        method_code, 
                        property_type, 
                        property_value)

        try:
            db.session.add(property)
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            return False

        return True
    

    def delete(self, method_code, property_type):
        try:
            row = db.session.query(PaymentMethodProperty).\
                filter(PaymentMethodProperty.method_code == method_code).\
                filter(PaymentMethodProperty.property_type == property_type).\
                delete()
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            return False
        
        return True
