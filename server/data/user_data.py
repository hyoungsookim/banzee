"""
"""

from server.utils import *
from server.models.user import User
from server.data import base
from server.data.helper import ConnectionHelper
from server.app import db


class UserData(base.Data):
    """
    User data class for accssing database
    """
    def __init__(self):
        pass

    def get_list(self):
        _rows = db.session.query(User).all()
        rows = [row.to_dict() for row in _rows]
        return rows


    def get(self, user_id):
        row = db.session.query(User).\
                filter(User.user_id == user_id).one_or_none()
        return row.to_dict()


    def create(self, user):
        if not isinstance(user, User):
            raise TypeError("user should be an instance of User class")

        try:
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
            return None

        return user


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
        except:
            db.session.rollback()
            return None

        return user


    def delete(self, user_id):
        try:
            db.session.query(User).\
                filter(User.user_id == user_id).\
                delete()
            db.session.commit()
        except:
            db.session.rollback()
            return False
        
        return True
