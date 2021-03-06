"""
"""

from sqlalchemy import Column, String, DateTime, Index
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.db_factory import db

#Base = declarative_base()
#metadata = Base.metadata


class UserAccount(db.Model):
    __tablename__ = 'mtt_uw_user_accounts'
    __table_args__ = (
        Index('mtd_uw_user_accounts_user_no', 'user_no', 'account_type', unique=True),
    )

    account_no      = db.Column(INTEGER, primary_key=True, autoincrement=True)
    account_id      = db.Column(String(50), nullable=False, unique=True)
    user_no         = db.Column(INTEGER, nullable=False)
    account_type    = db.Column(SMALLINT, nullable=False)
    account_status  = db.Column(SMALLINT, nullable=False)
    balance_amount  = db.Column(INTEGER, nullable=False)
    created_at      = db.Column(DateTime, nullable=False)
    updated_at      = db.Column(DateTime, nullable=False)


    def __init__(self, account_type=None, balance_amount=None):
        #self.user_no = user_no
        self.account_type = account_type
        self.account_status = 200
        self.balance_amount = balance_amount
        self.created_at = get_current_datetime_str()
        self.updated_at = get_current_datetime_str()


    def to_dict(self, output_attrs=None):
        """Returns the model attributes as a dict
s        :output_attrs: list that includes attributes to convert
        """
        if output_attrs:
            return {col.name: getattr(self, col.name) 
                        for col in self.__table__.columns 
                            if col.name in output_attrs}

        return {col.name: getattr(self, col.name) 
                    for col in self.__table__.columns}
