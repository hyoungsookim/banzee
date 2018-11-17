"""
"""

from server.utils import *
from server.models.transaction import Transaction
from server.data.transaction_data import TransactionData
from server.controller import ControllerBase


class TransactionController(ControllerBase):
    _trxData = TransactionData()

    def __init__(self):
        pass


    def get_list(self, account_id, q, offset=0, fetch=20):
        trx_list = None

        try:
            trx_list = self._trxData.get_list(account_id, q, offset, fetch)
        except:
            raise

        return trx_list


    def get(self, trx_id):
        trx_dict = None

        try:
            trx_dict = self._trxData.get(trx_id)
        except:
            raise

        return trx_dict


    def deposit_fund(self, 
                     sender_id, 
                     recipient_account_id, 
                     deposit_type, 
                     deposit_amount, 
                     reason=None):
        trx_id = self._trxData.deposit_fund(
                                sender_id, 
                                recipient_account_id,
                                deposit_type, 
                                deposit_amount, 
                                reason)        
        return self.get(trx_id)


    def withdraw_fund(self, 
                     account_id, 
                     withdrawal_amount, 
                     source_transaction_id, 
                     reason):
        self._trxData.withdraw_fund(account_id, withdrawal_amount, source_transaction_id, reason)

