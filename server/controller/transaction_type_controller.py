"""
"""

from server.utils import *
from server.models.transaction_type import TransactionType
from server.data.transaction_type_data import TransactionTypeData


class TransactionTypeController(object):
    typeData = TransactionTypeData()

    def __init__(self):
        pass

    def get_list(self):
        return self.typeData.get_list()

    def get(self, trx_type):
        return self.typeData.get(trx_type)

    def create(self, transactionType):
        return self.typeData.create(transactionType)

    def update(self, transactionType):
        return self.typeData.update(transactionType)

    def delete(self, trx_type):
        return self.typeData.delete(trx_type)

