"""
"""

from server.utils import *
from server.models.user import User
from server.models.user_account import UserAccount
from server.data.user_data import UserData
from server.data.user_account_data import UserAccountData


class UserController(object):

    def __init__(self):
        pass

    def get_list(self, q, offset=0, fetch=20):
        pass
    
    def get(self, user_id):
        pass

    def create(self, user):
        pass

    def update(self, user):
        pass

    def delete(self, user_id):
        pass

    def get_accounts(self, user_id):
        pass

    def open_account(self, user_id):
        pass
    
    def deposit(self, account_no, amount):
        pass
    
    def withdraw(self, account_no, amount):
        pass
