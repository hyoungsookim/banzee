"""
"""

from server.utils import *
from server.models.transaction import Transaction
from server.data.transaction_data import TransactionData


class TransactionController(object):
    _trxData = TransactionData()

    def __init__(self):
        pass


    def get_list(self, q, offset=0, fetch=20):
        trx_list = None

        try:
            trx_list = self._trxData.get_list(q, offset, fetch)
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
        print(trx_id)
        return self.get(trx_id)


    def withraw_fund(self, trx_id):
        pass

