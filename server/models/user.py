"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.app import db

#Base = declarative_base()
#metadata = Base.metadata


class User(db.Model):
    __tablename__ = 'mtt_uw_users'

    user_no         = db.Column(INTEGER, primary_key=True, autoincrement=True)
    user_id         = db.Column(String(50), nullable=False, unique=True)
    partner_id      = db.Column(String(50), nullable=False)
    user_status     = db.Column(SMALLINT, nullable=False)
    user_type       = db.Column(SMALLINT, nullable=False)
    user_level      = db.Column(SMALLINT, nullable=False)
    first_name      = db.Column(String(50), nullable=False)
    last_name       = db.Column(String(50), nullable=False)
    created_at      = db.Column(DateTime, nullable=False)
    updated_at      = db.Column(DateTime, nullable=False)

    def __init__(self, user_id, partner_id, user_status, user_type, user_level, first_name, last_name):
        self.user_id = user_id
        self.partner_id = partner_id
        self.user_status = user_status
        self.user_type = user_type
        self.user_level = user_level
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = get_current_datetime_str()
        self.updated_at = get_current_datetime_str()

    def to_dict(self, output_attrs=None):
        """Returns the model attributes as a dict
        :output_attrs: list that includes attributes to convert
        """
        if output_attrs:
            return {col.name: getattr(self, col.name) 
                        for col in self.__table__.columns 
                            if col.name in output_attrs}

        return {col.name: getattr(self, col.name) 
                    for col in self.__table__.columns}
