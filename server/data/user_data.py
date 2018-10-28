"""
"""

from sqlalchemy.exc import OperationalError

from server.utils import *
from server.models.user import User
from server.data import base
from server.data.helper import ConnectionHelper
from server.db_factory import db
from server.exceptions import *


class UserData(base.Data):
    """
    User data class for accssing database
    """
    def __init__(self):
        pass

    def get_list(self, q, offset=0, fetch=20):
        try:
            _rows = db.session.query(User).all()

        except OperationalError as ex:
            raise InternalServerError(ex)

        rows = [row.to_dict() for row in _rows]

        return rows


    def get(self, user_id):
        try:
            row = db.session.query(User).\
                    filter(User.user_id == user_id).one_or_none()

            if not row:
                raise ResourceNotFoundException

        except OperationalError as ex:
            raise InternalServerError(ex)

        return row.to_dict()


    def create(self, user):
        if not isinstance(user, User):
            raise TypeError("user should be an instance of User class")

        params = { 
            "user_id": user.user_id, 
            "partner_id": user.partner_id, 
            "first_name": user.first_name, 
            "last_name": user.last_name 
        }

        try:
            db.session.execute("call mtp_uw_create_user(:user_id, :partner_id, :first_name, :last_name, @user_no, @error_code)", params)
            res = db.session.execute("select @user_no, @error_code").fetchone()
            db.session.commit()

            user_no = int(res[0])
            error_code = int(res[1])

            if (error_code != 0):
                raise BanzeeException(error_code)

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raise

        return user.to_dict()


    def update(self, user):
        if not isinstance(user, User):
            raise TypeError("user should be an instance of User class")

        try:
            db.session.query(User).\
                filter(User.user_id == user.user_id).\
                update({
                    "user_status": user.user_status,
                    "user_type": user.user_type,
                    "user_level": user.user_level,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "updated_at": get_current_datetime_str()
                })
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raise

        return user.to_dict()


    def delete(self, user_id):
        try:
            db.session.query(User).\
                filter(User.user_id == user_id).\
                delete()
            db.session.commit()

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            return False
        
        return True
