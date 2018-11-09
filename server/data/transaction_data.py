"""
"""

from sqlalchemy.exc import OperationalError

from server.utils import *
from server.models.transaction import Transaction
from server.data import base
from server.data.helper import ConnectionHelper
from server.db_factory import db
from server.exceptions import *


class TransactionData(base.Data):
    """
    Transaction data class for accssing database
    """
    def __init__(self):
        pass


    def get_list(self, q=None, offset=0, fetch=20):
        _rows = None

        try:
            _rows = db.session.query(Transaction).all()

        except OperationalError as ex:
            raise InternalServerError(ex)

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
            #db.session.commit()

        except:
            #db.session.rollback()
            raise

        return trx_id
