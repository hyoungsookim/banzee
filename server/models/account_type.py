"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.db_factory import db

#Base = declarative_base()
#metadata = Base.metadata


class AccountType(db.Model):
    __tablename__ = 'mtt_md_account_types'

    account_type                = db.Column(SMALLINT, primary_key=True)
    account_type_name           = db.Column(String(50), nullable=False)
    account_type_status         = db.Column(SMALLINT, nullable=False)
    created_at                  = db.Column(DateTime, nullable=False)
    updated_at                  = db.Column(DateTime, nullable=False)
    account_type_description    = db.Column(String(250), nullable=True)

    def __init__(self, account_type, account_type_name, account_type_status=200, account_type_description=None):
        self.account_type = account_type
        self.account_type_name = account_type_name
        self.account_type_status = account_type_status
        self.created_at = get_current_datetime_str()
        self.updated_at = get_current_datetime_str()
        self.account_type_description = account_type_description

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
