"""
"""

from server.utils import *
from server.models.user import User
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


    def get_list(self, user_id=None):
        if not user_id:
            user_no = self._find_user_no(user_id)
            rows = db.session.query(UserAccount).filter_by(user_no=user_no)
        else:
            rows = db.session.query(UserAccount).all()

        return rows


    def get(self, account_no, user_id):
        user_no = self._find_user_no(user_id)
        row = db.session.query(UserAccount).\
                filter_by(account_no=account_no, user_no=user_no)
        return row


    def open(self, user_id):
        try:
            user_no = self._find_user_no(user_id)
            # Open a reward account
            userAccount = UserAccount(user_no=user_no, account_type=1, balance_amount=0)
            db.session.add(userAccount)
            db.session.commit()
        except:
            db.session.rollback()
            
        return True


    def change_status(self, account_no, user_id, new_status):
        user_no = self._find_user_no(user_id)
        db.session.query(UserAccount).\
            filter(UserAccount.account_no == account_no).\
            filter(UserAccount.user_no == user_no).\
            update({
                "account_status": new_status
            })


    def deposit(self, account_no, user_id, amount):
        try:
            user_no = self._find_user_no(user_id)
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
            user_no = self._find_user_no(user_id)
            pass
        except:
            db.session.rollback()
            return False

        return True


    def _find_user_no(self, user_id):
        row = User.query(User.user_no).\
                filter(User.user_id == user_id).one_or_none()
        if not row:
            user_no = row.user_no

        return user_no
