"""
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, SmallInteger, DateTime

Base = declarative_base()


class UserAccount(Base):
    __tablename__ = 'mtt_uw_user_accounts'

    account_no      = Column(Integer, primary_key=True)
    user_no         = Column(Integer, nullable=False)
    account_type    = Column(SmallInteger, nullable=False)
    balance_amount  = Column(Integer, nullable=False)
    updated_at      = Column(DateTime, nullable=False)

    def __init__(self, user_no, account_type, balance_amount=0):
        self.user_no = user_no
        self.account_type = account_type
        self.balance_amount = balance_amount
