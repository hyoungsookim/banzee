"""
"""

from sqlalchemy.exc import OperationalError

from server.utils import *
from server.models.user import User
from server.models.user_account import UserAccount
from server.data import base
from server.data.helper import ConnectionHelper
from server.db_factory import db
from server.exceptions import *


class UserAccountData(base.Data):
    """
    User Account data class for accssing database
    """
    def __init__(self):
        pass


    def get_list(self, user_id, q, offset=0, fetch=20):
        try:
            user_no = self._find_user_no(user_id)
            _rows = db.session.query(UserAccount).\
                        filter(UserAccount.user_no == user_no)

        except OperationalError as ex:
            raise InternalServerError(ex)

        rows = [row.to_dict() for row in _rows]

        return rows


    def get(self, user_id, account_id):
        try:
            user_no = self._find_user_no(user_id)
            row = db.session.query(UserAccount).\
                    filter(UserAccount.account_id == account_id).\
                    filter(UserAccount.user_no == user_no).one_or_none()

        except OperationalError as ex:
            raise InternalServerError(ex)

        return row.to_dict()


    def open(self, user_id, account_type):
        params = { 
            "user_id": user_id, 
            "account_type": account_type
        }

        try:
            db.session.execute("call mtp_uw_open_account(:user_id, :account_type, @account_id, @error_code)", params)
            res = db.session.execute("select cast(@account_id as char(36)), @error_code").fetchone()

            error_code = int(res[1])
            if (error_code != 0):
                raise BanzeeException(error_code)

            account_id = res[0].decode()
            db.session.commit()

        except:
            db.session.rollback()
            raise
        
        return account_id


    def change_status(self, user_id, account_id, new_status):
        try:
            user_no = self._find_user_no(user_id)
            db.session.query(UserAccount).\
                filter(UserAccount.account_id == account_id).\
                filter(UserAccount.user_no == user_no).\
                update({
                    "account_status": new_status
                })
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raise

        return True


    def _find_user_no(self, user_id):
        user_no = None

        row = db.session.query(User.user_no).\
                filter(User.user_id == user_id).one_or_none()
        if row:
            user_no = row.user_no

        return user_no
