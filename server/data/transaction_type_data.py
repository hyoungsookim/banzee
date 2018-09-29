"""
"""

from server.utils import *
from server.models.transaction_type import TransactionType
from server.data import base
from server.data.helper import ConnectionHelper
from server.app import db


class TransactionTypeData(base.Data):
    """
    TransactionType data class for accssing database
    """
    def __init__(self):
        pass


    def get_list(self):
        _rows = db.session.query(TransactionType).all()
        rows = [row.to_dict() for row in _rows]
        return rows


    def get(self, trx_type):
        row = db.session.query(TransactionType).\
                filter(TransactionType.trx_type == trx_type).one_or_none()
        return row.to_dict()


    def create(self, transactionType):
        if not isinstance(transactionType, TransactionType):
            raise TypeError("transactionType should be an instance of TransactionType class")

        try:
            db.session.add(transactionType)
            db.session.commit()
        except:
            db.session.rollback()
            raise
            return None

        return transactionType


    def update(self, transactionType):
        if not isinstance(transactionType, TransactionType):
            raise TypeError("transactionType should be an instance of TransactionType class")

        try:
            db.session.query(TransactionType).\
                filter(TransactionType.trx_type == transactionType.trx_type).\
                update({
                    "trx_type_name": transactionType.trx_type_name,
                    "updated_at": get_current_datetime_str(),
                    "trx_type_description": transactionType.trx_type_description
                })
            db.session.commit()
        except:
            db.session.rollback()
            return None

        return transactionType


    def delete(self, trx_type):
        try:
            db.session.query(TransactionType).\
                filter(TransactionType.trx_type == trx_type).\
                delete()
            db.session.commit()
        except:
            db.session.rollback()
            return False
        
        return True
