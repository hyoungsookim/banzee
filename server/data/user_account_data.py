"""
"""

from server.utils import *
from server.models.user_account import UserAccount
from server.data import base
from server.data.helper import ConnectionHelper
from server.app import db


class UserAccountData(base.Data):
    """
    User Account data class for accssing database
    """
    def __init__(self):
        pass


    def get_list(self):
        rows = UserAccount.query.all()
        return rows


    def get_list_by_user_id(self, user_id):
        pass


    def get(self, account_no, user_id):
        row = UserAccount.query.filter_by(account_no=account_no)
        return row


    def open(self, user_id):
        try:
            #db.session.add(userAccount)
            #db.session.commit()
        except:
            db.session.rollback()
            
        return True


    def change_status(self, account_no, user_id, new_status):
        pass


    def deposit(self, account_no, user_id, amount):
        try:
            #db.session.query(UserAccount).filter_by(account_no=userAccount.account_no).\
            #    update({
            #                "balance_amount": userAccount.balance_amount,
            #                "updated_at": get_current_datetime_str()
            #            })
            #db.session.commit()
        except:
            db.session.rollback()
            return False

        return True


    def withdraw(self, account_no, user_id, amount):
        try:
            pass
        except:
            db.session.rollback()
            return False

        return True
