"""
"""

from server.utils import *
from server.models.account_type import AccountType
from server.data.account_type_data import AccountTypeData
from server.exceptions import *


class AccountTypeController(object):
    _typeData = AccountTypeData()

    def __init__(self):
        pass


    def get_list(self, q, offset=0, fetch=20):
        type_list = None
        try:
            type_list = self._typeData.get_list(q, offset, fetch)
        except:
            raise

        return type_list

    
    def get(self, account_type):
        type_dict = None
        try:
            type_dict = self._typeData.get(account_type)
        except:
            raise

        return type_dict


    def create(self, accountType):
        type_dict = None
        try:
            type_dict = self._typeData.create(accountType)
        except:
            raise

        return type_dict


    def update(self, accountType):
        type_dict = None
        try:
            type_dict = self._typeData.update(accountType)
        except:
            raise

        return type_dict 

    def delete(self, account_type):
        return self._typeData.delete(account_type)
