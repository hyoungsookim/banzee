"""
"""

from sqlalchemy.exc import OperationalError

from server.utils import *
from server.models.transaction import Transaction
from server.models.user_account import UserAccount
from server.data import DataBase
from server.data.helper import ConnectionHelper
from server.db_factory import db
from server.exceptions import *


class TransactionData(DataBase):
    """
    Transaction data class for accssing database
    """
    def __init__(self):
        pass


    def get_list(self, account_id=None, q=None, offset=0, fetch=20):
        _rows = None

        try:
            if account_id:
                account_no = self._find_account_no(account_id)
                _rows = db.session.query(Transaction).\
                            filter(Transaction.account_no == account_no).one_or_none()
            else:
                _rows = db.session.query(Transaction).all()

        except OperationalError as ex:
            raise InternalServerError(ex)

        rows = None
        if _rows:
            rows = [row.to_dict() for row in _rows]

        return rows


    def get(self, trx_id):
        try:
            row = db.session.query(Transaction).\
                    filter(Transaction.trx_id == trx_id).one_or_none()

            if not row:
                raise ResourceNotFoundException

        except OperationalError as ex:
            raise InternalServerError(ex)

        return row.to_dict()


    def deposit_fund(self, sender_id, recipient_account_id, deposit_type, deposit_amount, reason=None):
        params = { 
            "sender_id": sender_id, 
            "recipient_account_id": recipient_account_id, 
            "deposit_type": deposit_type, 
            "deposit_amount": deposit_amount,
            "reason": reason 
        }

        try:
            db.session.execute("call mtp_tx_deposit_fund(:sender_id, :recipient_account_id, :deposit_type, :deposit_amount, :reason, @trx_id, @error_code)", params)
            res = db.session.execute("select @trx_id, @error_code").fetchone()

            error_code = int(res[1])
            if (error_code != 0):
                raise BanzeeException(error_code)

            trx_id = res[0].decode()

        except:
            raise

        return trx_id


    def withdraw_fund(self, account_id, withdrawal_amount, source_transaction_id, reason=None):
        params = { 
            "account_id": account_id, 
            "withdrawal_type": 2000,
            "withdrawal_amount": withdrawal_amount,
            "source_transaction_id": source_transaction_id, 
            "reason": reason 
        }

        try:
            db.session.execute("call mtp_tx_withdraw_fund(:account_id, :withdrawal_type, :withdrawal_amount, :source_transaction_id, :reason, @error_code)", params)
            res = db.session.execute("select @error_code").fetchone()

            error_code = int(res[0])
            if (error_code != 0):
                raise BanzeeException(error_code)

        except:
            raise


    def _find_account_no(self, account_id):
        account_no = None

        row = db.session.query(UserAccount.account_no).\
                filter(UserAccount.account_id == account_id).one_or_none()
        if row:
            account_no = row.account_no

        return account_no
