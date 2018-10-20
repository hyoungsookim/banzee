"""
"""

from sqlalchemy.exc import OperationalError

from server.utils import *
from server.models.transaction_type import TransactionType
from server.data import base
from server.data.helper import ConnectionHelper
from server.db_factory import db
from server.exceptions import *


class TransactionTypeData(base.Data):
    """
    TransactionType data class for accssing database
    """
    def __init__(self):
        pass


    def get_list(self, q=None, offset=0, fetch=20):
        _rows = None
        try:
            _rows = db.session.query(TransactionType).all()

        except OperationalError as ex:
            raise InternalServerError(ex)

        rows = [row.to_dict() for row in _rows]

        return rows


    def get(self, trx_type):
        try:
            row = db.session.query(TransactionType).\
                    filter(TransactionType.trx_type == trx_type).one_or_none()

            if not row:
                raise ResourceNotFoundException

        except OperationalError as ex:
            raise InternalServerError(ex)

        return row.to_dict()


    def create(self, transactionType):
        if not isinstance(transactionType, TransactionType):
            raise TypeError("transactionType should be an instance of TransactionType class")

        try:
            db.session.add(transactionType)
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raise

        return transactionType.to_dict()


    def update(self, transactionType):
        if not isinstance(transactionType, TransactionType):
            raise TypeError("transactionType should be an instance of TransactionType class")

        try:
            #db.session.query(TransactionType).\
            #    filter(TransactionType.trx_type == transactionType.trx_type).\
            #    update({
            #        "trx_type_name": transactionType.trx_type_name,
            #        "updated_at": get_current_datetime_str(),
            #        "trx_type_description": transactionType.trx_type_description
            #    })
            transactionType.updated_at = get_current_datetime_str()
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raise

        return transactionType.to_dict()


    def delete(self, trx_type):
        try:
            db.session.query(TransactionType).\
                filter(TransactionType.trx_type == trx_type).\
                delete()
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raise
        
        return True
