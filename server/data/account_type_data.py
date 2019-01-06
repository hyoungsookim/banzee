"""
"""

from sqlalchemy.exc import OperationalError

from server.utils import *
from server.models.account_type import AccountType
from server.data import DataBase
from server.data.helper import ConnectionHelper
from server.db_factory import db
from server.exceptions import *


class AccountTypeData(DataBase):
    """
    AccountType data class for accssing database
    """
    def __init__(self):
        pass


    def get_list(self, q=None, offset=0, fetch=20):
        _rows = None
        try:
            _rows = db.session.query(AccountType).all()

        except OperationalError as ex:
            raise InternalServerError(ex)

        rows = [row.to_dict() for row in _rows]

        return rows


    def get(self, account_type):
        try:
            row = db.session.query(AccountType).\
                    filter(AccountType.account_type == account_type).one_or_none()

            if not row:
                raise ResourceNotFoundException

        except OperationalError as ex:
            raise InternalServerError(ex)

        return row.to_dict()


    def create(self, accountType):
        if not isinstance(accountType, AccountType):
            raise TypeError("accountType should be an instance of AccountType class")

        try:
            db.session.add(accountType)
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raise

        return accountType.to_dict()


    def update(self, accountType):
        if not isinstance(accountType, AccountType):
            raise TypeError("accountType should be an instance of AccountType class")

        try:
            #db.session.query(TransactionType).\
            #    filter(TransactionType.trx_type == transactionType.trx_type).\
            #    update({
            #        "trx_type_name": transactionType.trx_type_name,
            #        "updated_at": get_current_datetime_str(),
            #        "trx_type_description": transactionType.trx_type_description
            #    })
            accountType.updated_at = get_current_datetime_str()
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raises

        return accountType.to_dict()


    def delete(self, account_type):
        try:
            db.session.query(AccountType).\
                filter(AccountType.account_type == account_type).\
                delete()
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raise
        
        return True
