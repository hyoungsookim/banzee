"""
"""

from sqlalchemy import Column, String, DateTime, Index
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UserAccount(Base):
    __tablename__ = 'mtt_uw_user_accounts'
    __table_args__ = (
        Index('mtd_uw_user_accounts_user_no', 'user_no', 'account_type', unique=True),
    )

    account_no      = Column(INTEGER, primary_key=True)
    user_no         = Column(INTEGER, nullable=False)
    account_type    = Column(SMALLINT, nullable=False)
    balance_amount  = Column(INTEGER, nullable=False)
    updated_at      = Column(DateTime, nullable=False)

    def __init__(self, user_no, account_type, balance_amount=0):
        self.user_no = user_no
        self.account_type = account_type
        self.balance_amount = balance_amount
