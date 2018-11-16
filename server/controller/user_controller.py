"""
"""

from server.utils import *
from server.models.user import User
from server.models.user_account import UserAccount
from server.data.user_data import UserData
from server.data.user_account_data import UserAccountData
from server.data.transaction_data import TransactionData
from server.controller import ControllerBase
from server.exceptions import *


class UserController(ControllerBase):
    _userData = UserData()
    _userAccountData = UserAccountData()

    def __init__(self):
        pass


    def get_list(self, q, offset=0, fetch=20):
        user_list = None
        try:
            user_list = self._userData.get_list(q, offset, fetch)
        except:
            raise

        return user_list

    
    def get(self, user_id):
        user_dict = None
        try:
            user_dict = self._userData.get(user_id)
        except:
            raise

        return user_dict


    def create(self, user):
        user_dict = None
        try:
            user_dict = self._userData.create(user)
        except:
            raise

        return user_dict


    def update(self, user):
        user_dict = None
        try:
            user_dict = self._userData.update(user)
        except:
            raise

        return user_dict


    def delete(self, user_id):
        return self._userData.delete(user_id)


    def get_account_list(self, user_id):
        account_list = None
        try:
            account_list = self._userAccountData.get_list(user_id, q=None, offset=0, fetch=20)
        except:
            raise

        return account_list


    def get_account(self, user_id, account_id):
        account_dict = None
        try:
            account_dict = self._userAccountData.get(user_id, account_id)
        except:
            raise

        return account_dict


    def open_account(self, user_id, account_type):
        account_dict = None
        try:
            account_id = self._userAccountData.open(user_id, account_type)
            account_dict = self._userAccountData.get(user_id, account_id)
        except:
            raise

        return account_dict


    def close_account(self, user_id, account_id):
        return self.change_account_status(user_id, account_id, -1)


    def change_account_status(self, user_id, account_id, new_status):
        return self._userAccountData.change_status(user_id, account_id, new_status)


    def get_transaction_list(self, account_id):
        trx_list = None

        try:
            trx_list = TransactionData().get_list(
                                            account_id, 
                                            q=None, 
                                            offset=0, 
                                            fetch=20)
        except:
            raise

        return trx_list
    
